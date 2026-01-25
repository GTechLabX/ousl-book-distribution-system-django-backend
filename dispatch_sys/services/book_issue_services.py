import uuid
from django.db import transaction, models
from django.utils import timezone
from dispatch_sys.models import Student, CenterBook, ReceivedBook
from auth_sys.models import CustomUser


def book_issue_service(sender, data, callback, **kwargs):
    # 1. Data Extraction
    admin_uuid_str = data.get("admin_uuid")
    student_nic = data.get("student_nic")
    book_id = data.get("book_id")
    course_id = data.get("course_id") or book_id

    # --- PRE-TRANSACTION VALIDATIONS ---

    # 2. Validate Admin and Center
    try:
        admin_user = CustomUser.objects.select_related('userprofile__center_id').get(
            uuid=uuid.UUID(admin_uuid_str)
        )
        admin_center = admin_user.userprofile.center_id
    except (CustomUser.DoesNotExist, ValueError, TypeError):
        return callback({"success": False, "error": "Invalid Admin credentials or UUID format."})

    if not admin_center:
        return callback({"success": False, "error": "Admin user is not assigned to any regional center."})

    # 3. Get Student
    try:
        student = Student.objects.get(nic=student_nic)
    except Student.DoesNotExist:
        return callback({"success": False, "error": f"Student with NIC {student_nic} not found."})

    # 4. Duplicate Prevention (Check before starting transaction)
    if ReceivedBook.objects.filter(student=student, center_book__books_id=book_id).exists():
        return callback({"success": False, "error": f"Book ID {book_id} has already been issued to this student."})

    # 5. Preliminary Inventory Check (Quick check without locking)
    center_book_exists = CenterBook.objects.filter(center_id=admin_center.id, books_id=book_id).first()

    if not center_book_exists:
        return callback({"success": False, "error": f"Book ID {book_id} is not allocated to {admin_center.c_name}."})

    if center_book_exists.allocation_quantity <= 0:
        return callback({"success": False, "error": f"Insufficient stock for Book {book_id} in {admin_center.c_name}."})

    # --- START DATABASE TRANSACTION ---
    # Everything is valid, now we lock the row and update
    try:
        with transaction.atomic():
            # Re-fetch with select_for_update to handle concurrency safely
            center_book = CenterBook.objects.select_for_update().get(id=center_book_exists.id)

            # Double check stock inside the lock just in case someone took the last one
            # in the millisecond between our check and our lock
            if center_book.allocation_quantity <= 0:
                return callback({"success": False, "error": "Stock was depleted by another request."})

            # 6. Create Issuance Record
            rb = ReceivedBook.objects.create(
                center_book=center_book,
                student=student,
                center_book_course_id=course_id,
                is_received=True,
                date=timezone.now().date(),
                time=timezone.now().time()
            )

            # 7. Update Stock
            center_book.allocation_quantity = models.F('allocation_quantity') - 1
            center_book.save()

            return callback({
                "success": True,
                "message": f"Successfully issued {book_id} to {student.student_name}",
                "data": {"id": rb.id}
            })

    except Exception as e:
        print(f"TRANSACTION ERROR: {str(e)}")
        return callback({"success": False, "error": "Database error during issuance. Please try again."})