import uuid
from django.db import transaction, models
from django.utils import timezone
from django.core.mail import send_mail
from dispatch_sys.models import Student, CenterBook, ReceivedBook, Book
from auth_sys.models import CustomUser
from django.conf import settings

from events.signals.student_acc_created_signals import book_issue_required


def book_issue_service(sender, data, callback, **kwargs):
    admin_uuid_str = data.get("admin_uuid")
    student_nic = data.get("student_nic")
    course_id = data.get("book_id")  # this is actually course_id in your payload

    # --- 1. Find the Book linked to this course ---
    try:
        book = Book.objects.get(course_id=course_id)
    except Book.DoesNotExist:
        return callback({"success": False, "error": f"No book found for course ID {course_id}"})

    # --- 2. Validate Admin and Center ---
    try:
        admin_user = CustomUser.objects.select_related('userprofile__center_id').get(uuid=uuid.UUID(admin_uuid_str))
        admin_center = admin_user.userprofile.center_id
    except (CustomUser.DoesNotExist, ValueError, TypeError):
        return callback({"success": False, "error": "Invalid admin credentials or UUID."})

    if not admin_center:
        return callback({"success": False, "error": "Admin user is not assigned to any center."})

    # --- 3. Get Student ---
    try:
        student = Student.objects.get(nic=student_nic)
    except Student.DoesNotExist:
        return callback({"success": False, "error": f"Student with NIC {student_nic} not found."})

    # --- 4. Prevent duplicate issuance ---
    if ReceivedBook.objects.filter(student=student, center_book__books_id=book.id).exists():
        return callback({"success": False, "error": f"Book '{book.name}' already issued to this student."})

    # --- 5. Check center allocation, approval, and stock ---
    center_book_qs = CenterBook.objects.filter(center_id=admin_center.id, books_id=book.id)
    if not center_book_qs.exists():
        return callback({"success": False, "error": f"Book '{book.name}' is not allocated to {admin_center.c_name}."})

    center_book_exists = center_book_qs.first()

    if not center_book_exists.approved:
        return callback({"success": False, "error": f"Book '{book.name}' is still in PENDING stage. Must approve to issue."})

    if center_book_exists.allocation_quantity <= 0:
        return callback({"success": False, "error": f"No stock left for '{book.name}' at {admin_center.c_name}."})

    # --- 6. Issue the book transactionally ---
    try:
        with transaction.atomic():
            center_book = CenterBook.objects.select_for_update().get(id=center_book_exists.id)

            if center_book.allocation_quantity <= 0:
                return callback({"success": False, "error": "Stock was depleted by another request."})

            received_book = ReceivedBook.objects.create(
                center_book=center_book,
                student=student,
                center_book_course_id=course_id,
                is_received=True,
                date=timezone.now().date(),
                time=timezone.now().time()
            )

            # Decrement allocation
            center_book.allocation_quantity = models.F('allocation_quantity') - 1
            center_book.save()

            # --- 7. Send email to student ---
            if student.email and student.email != "none":
                try:
                    book_issue_required.send(
                        sender=received_book,
                        student_id=student.id,
                        student_name=student.student_name,
                        email=student.email,
                        book_name=book.name,
                        course_code=book.course.course_code,
                        center_name=admin_center.c_name,
                        issue_date=received_book.date,
                        issue_time=received_book.time
                    )
                except Exception as e:
                    print(f"Email sending failed: {str(e)}")

            return callback({
                "success": True,
                "message": f"Successfully issued '{book.name}' to {student.student_name}",
                "data": {"id": received_book.id}
            })

    except Exception as e:
        print(f"TRANSACTION ERROR: {str(e)}")
        return callback({"success": False, "error": "Database error during issuance. Please try again."})
