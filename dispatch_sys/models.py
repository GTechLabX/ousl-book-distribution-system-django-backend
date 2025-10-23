from django.db import models


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


class DegreeProgram(models.Model):
    d_program = models.CharField(max_length=100, name="d_program")
    additional_info = models.CharField(max_length=1000, name="info")

    class Meta:
        db_table = "degree_program"

    def __str__(self):
        return f"Degree Program Name: {self.d_program}"


class District(models.Model):
    d_name = models.CharField(max_length=100, name="district_name")
    additional_info = models.CharField(max_length=1000, name="info")

    class Meta:
        db_table = "district"

    def __str__(self):
        return f"District name: {self.d_name}"


class Center(models.Model):
    c_name = models.CharField(name="center_name", max_length=100)
    tel_no = models.CharField(name="tel_no", max_length=12)

    class Meta:
        db_table = "center"

    def __str__(self):
        return f"Center name: {self.c_name}"


class Student(models.Model):
    student_name = models.CharField(max_length=500, name="student_name")
    nic = models.CharField(max_length=15, name="nic", null=False, unique=True)
    s_no = models.CharField(max_length=15, name="s_no")
    reg_no = models.CharField(max_length=15, name="reg_no")

    class Meta:
        db_table = "student"
        indexes = [
            models.Index(fields=["nic"]),
            models.Index(fields=["reg_no"]),
        ]

    def __str__(self):
        return f"Student name: {self.student_name}"
