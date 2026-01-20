from django.db import transaction
from django.utils import timezone
from dispatch_sys.models import  Student, CenterBook, ReceivedBook
from auth_sys.models import CustomUser
def book_issue_service(sender, data, callback, **kwargs):
    """
    Issue a book at the admin's center for one or more courses.
    Expects in `data`:
        - admin_uuid: CustomUser UUID (admin issuing the book)
        - student_nic: NIC of the student
        - book_id: ID of the book
        - course_ids: list of course IDs (1 or more)
    """
    admin_uuid = data.get("admin_uuid")
    student_nic = data.get("student_nic")
    book_id = data.get("book_id")
    course_ids = data.get("course_ids")  # must be a list

    # ✅ Basic validations
    if not admin_uuid:
        return callback({"success": False, "error": "Admin UUID is required"})
    if not student_nic:
        return callback({"success": False, "error": "Student NIC is required"})
    if not book_id:
        return callback({"success": False, "error": "Book ID is required"})
    if not course_ids or not isinstance(course_ids, list):
        return callback({"success": False, "error": "course_ids must be a list with one or more IDs"})

    try:
        with transaction.atomic():
            # 1️⃣ Get admin
            admin_user = CustomUser.objects.select_related("userprofile").get(uuid=admin_uuid)

            # 2️⃣ Get admin's center from UserProfile
            admin_center = getattr(admin_user.userprofile, "center_id", None)
            if not admin_center:
                return callback({"success": False, "error": "Admin has no center assigned"})

            # 3️⃣ Get student
            student = Student.objects.get(nic=student_nic)

            # 4️⃣ Lock center book row
            center_book = CenterBook.objects.select_for_update().get(
                center=admin_center,
                books_id=book_id,
                approved=True
            )

            # 5️⃣ Stock check for all courses
            if center_book.allocation_quantity < len(course_ids):
                return callback({"success": False, "error": "Not enough stock for all courses"})

            # 6️⃣ Create ReceivedBook for each course
            for course_id in course_ids:
                ReceivedBook.objects.create(
                    center_book=center_book,
                    student=student,
                    book_id=book_id,
                    center_book_course_id=course_id,
                    is_received=True,
                    date=timezone.now().date(),
                    time=timezone.now().time()
                )

            # 7️⃣ Decrease stock
            center_book.allocation_quantity -= len(course_ids)
            center_book.save()

            return callback({
                "success": True,
                "message": f"Book issued successfully for {len(course_ids)} course(s)"
            })

    except CustomUser.DoesNotExist:
        return callback({"success": False, "error": "Admin not found"})
    except Student.DoesNotExist:
        return callback({"success": False, "error": "Student not found"})
    except CenterBook.DoesNotExist:
        return callback({"success": False, "error": "Book not available in this center"})
    except Exception as e:
        return callback({"success": False, "error": str(e)})
