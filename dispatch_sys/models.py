import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from datetime import timedelta


def current_year():
    return datetime.date.today().year


class Faculty(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]

    faculty_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    dean_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='faculty_logos/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'faculty'
        ordering = ['name']
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return f"{self.name} ({self.faculty_code})"


class Department(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='departments')
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)

    status = models.BooleanField(default=True)  # True = active, False = inactive

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "departments"
        ordering = ["name"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class DegreeProgram(models.Model):
    d_program = models.CharField(max_length=100, name="d_program")
    additional_info = models.CharField(max_length=1000, name="info")
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name='degree_department')

    class Meta:
        db_table = "degree_program"

    def __str__(self):
        return f"Degree Program Name: {self.d_program}"


class Course(models.Model):
    name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=30, unique=True)

    additional_info = models.TextField(blank=True, null=True)

    years = models.IntegerField(default=1)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course"

    def __str__(self):
        return f"{self.course_code} — {self.name}"


class DegreeProgramCourse(models.Model):
    degree_program = models.ForeignKey(
        DegreeProgram,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    # optional extra fields
    year_offered = models.IntegerField(
        default=current_year,
        validators=[MinValueValidator(1900), MaxValueValidator(current_year())]
    )
    is_mandatory = models.BooleanField(default=True)

    class Meta:
        db_table = "degree_program_course"
        unique_together = ("degree_program", "course")

    def __str__(self):
        return f"{self.degree_program} — {self.course}"


class District(models.Model):
    district_name = models.CharField(max_length=100, db_column="d_name")
    info = models.CharField(max_length=1000, db_column="info")

    class Meta:
        db_table = "district"

    def __str__(self):
        return f"District name: {self.district_name}"


class Center(models.Model):
    c_name = models.CharField(name="c_name", max_length=100)
    tel_no = models.CharField(name="tel_no", max_length=12)
    district = models.ForeignKey('District', on_delete=models.CASCADE, related_name='center_district')

    class Meta:
        db_table = "center"

    def __str__(self):
        return f"Center name: {self.c_name}"


class Student(models.Model):
    student_name = models.CharField(max_length=500, name="student_name")
    nic = models.CharField(max_length=15, name="nic", null=False, unique=True)
    s_no = models.CharField(max_length=15, name="s_no")
    reg_no = models.CharField(max_length=15, name="reg_no")
    email = models.EmailField(name="email", default='none')
    district = models.ForeignKey('District', on_delete=models.CASCADE, related_name='student_district')
    center = models.ForeignKey('Center', on_delete=models.CASCADE, related_name='student_center')
    degree_program = models.ForeignKey("DegreeProgram", on_delete=models.CASCADE, related_name="student_degree")

    # courses = models.ManyToManyField(Course, through="StudentCourseRegistration", related_name="student_course")

    class Meta:
        db_table = "student"
        indexes = [
            models.Index(fields=["nic"]),
            models.Index(fields=["reg_no"]),
        ]

    def __str__(self):
        return f"Student name: {self.student_name}"


class StudentCourse(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    # registration details
    # register_year = models.IntegerField()
    register_year = models.IntegerField(
        default=current_year,
        validators=[MinValueValidator(1900), MaxValueValidator(current_year())]
    )
    enrollment_date = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    # optional academic info
    grade = models.CharField(max_length=5, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "student_course"
        unique_together = ("student", "course", "register_year")

    def save(self, *args, **kwargs):
        # auto-set expiry = 1 year after enrollment
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=365)

        # auto-deactivate if expired
        if self.expires_at < timezone.now():
            self.is_active = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.student_name} → {self.course.course_code} ({self.register_year})"


class Book(models.Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_books")
    printed_quantity = models.IntegerField(default=0)
    left_quantity = models.IntegerField(default=0)

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.name


class CenterBook(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )

    center = models.ForeignKey(
        Center,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='centerbook')
    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    approved = models.BooleanField(default=False)

    allocation_quantity = models.IntegerField(default=0)

    class Meta:
        db_table = "center_book"

    def __str__(self):
        return f" {self.center.c_name} - {self.date} at {self.time}"


class ReceivedBook(models.Model):
    center_book = models.ForeignKey(CenterBook, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    center_book_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_received = models.BooleanField(default=False)

    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = "received_book"

    def __str__(self):
        return f"Received: {self.is_received} on {self.date} at {self.time}"


# QR Code model
class StudentQRCode(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="qr_code"
    )
    qr_image = models.ImageField(upload_to='student_qr_codes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR Code for {self.student.student_name}"


#
# class BookReservation(models.Model):
#     RESERVATION_STATUS = [
#         ('PENDING', 'Pending'),
#         ('APPROVED', 'Approved'),
#         ('REJECTED', 'Rejected'),
#         ('COLLECTED', 'Collected'),
#         ('CANCELLED', 'Cancelled'),
#         ('EXPIRED', 'Expired'),
#     ]
#
#     student = models.ForeignKey(
#         'dispatch_sys.Student',
#         on_delete=models.CASCADE,
#         related_name='book_reservations'
#     )
#
#     book = models.ForeignKey(
#         'dispatch_sys.Book',
#         on_delete=models.CASCADE,
#         related_name='reservations'
#     )
#
#     center = models.ForeignKey(
#         'dispatch_sys.Center',
#         on_delete=models.CASCADE,
#         related_name='book_reservations'
#     )
#
#     reservation_date = models.DateTimeField(
#         auto_now_add=True
#     )
#
#     expected_pickup_date = models.DateField()
#
#     status = models.CharField(
#         max_length=20,
#         choices=RESERVATION_STATUS,
#         default='PENDING'
#     )
#
#     remarks = models.TextField(
#         blank=True,
#         null=True
#     )
#
#     is_active = models.BooleanField(
#         default=True
#     )
#
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )
#
#     updated_at = models.DateTimeField(
#         auto_now=True
#     )
#
#     class Meta:
#         db_table = "book_reservations"
#         ordering = ['-created_at']
#         unique_together = ('student', 'book', 'status')
#
#     def __str__(self):
#         return f"{self.student} → {self.book} ({self.status})"


class BookReservation(models.Model):
    RESERVATION_STATUS = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('COLLECTED', 'Collected'),
        ('CANCELLED', 'Cancelled'),
        ('EXPIRED', 'Expired'),
    ]

    student = models.ForeignKey(
        'dispatch_sys.Student',
        on_delete=models.CASCADE,
        related_name='book_reservations'
    )

    book = models.ForeignKey(
        'dispatch_sys.Book',
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    center = models.ForeignKey(
        'dispatch_sys.Center',
        on_delete=models.CASCADE,
        related_name='book_reservations'
    )

    reservation_date = models.DateTimeField(auto_now_add=True)

    expected_pickup_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=RESERVATION_STATUS,
        default='PENDING'
    )

    remarks = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    expires_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "book_reservations"
        ordering = ['-created_at']
        unique_together = ('student', 'book', 'is_active')  # better than status

    def save(self, *args, **kwargs):
        # Automatically set expiration (example: 3 days after reservation)
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=3)

        super().save(*args, **kwargs)

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    def mark_as_expired(self):
        if self.is_expired and self.status not in ['COLLECTED', 'CANCELLED']:
            self.status = 'EXPIRED'
            self.is_active = False
            self.save()

    def __str__(self):
        return f"{self.student} → {self.book} ({self.status})"
