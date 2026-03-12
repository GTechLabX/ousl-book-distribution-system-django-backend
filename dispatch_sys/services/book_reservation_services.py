from django.shortcuts import get_object_or_404

from auth_sys.models import CustomUser
from dispatch_sys.models import BookReservation, StudentCourse, Student
from dispatch_sys.serializers.book_reservation_serializer import BookReservationSerializer


def book_reservation_add_service(sender, data, callback, **kwargs):
    serializer = BookReservationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def book_reservation_update_service(sender, pk, data, callback, **kwargs):
    try:
        reservation = BookReservation.objects.get(pk=pk)
        serializer = BookReservationSerializer(reservation, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return callback({"success": True, "data": serializer.data})
        return callback({"success": False, "errors": serializer.errors})
    except BookReservation.DoesNotExist:
        return callback({"success": False, "message": "Reservation not found"})


def book_reservation_delete_service(sender, pk, callback, **kwargs):
    try:
        BookReservation.objects.get(pk=pk).delete()
        return callback({"success": True, "message": "Deleted successfully"})
    except BookReservation.DoesNotExist:
        return callback({"success": False, "message": "Reservation not found"})


def book_reservation_show_service(sender, pk, callback, **kwargs):
    try:
        reservation = BookReservation.objects.get(pk=pk)
        serializer = BookReservationSerializer(reservation)
        return callback({"success": True, "data": serializer.data})
    except BookReservation.DoesNotExist:
        return callback({"success": False, "message": "Reservation not found"})


def book_reservation_all_service(sender, callback, **kwargs):
    reservations = BookReservation.objects.all()
    serializer = BookReservationSerializer(reservations, many=True)
    return callback({"success": True, "data": serializer.data})


#
# def make_book_reservation_service(sender, uuid, callback, **kwargs):
#     """
#     Get the student and their registered courses based on student pk.
#     """
#     try:
#
#         student = Student.objects.get(pk=pk)
#
#         registered_courses = StudentCourse.objects.filter(
#             student=student,
#             is_active=True
#         ).select_related("course")  # optional, to reduce DB queries
#
#         data = {
#             # "student": {
#             #     "id": student.id,
#             #     "name": student.student_name,
#             #     "reg_no": student.reg_no,
#             #     "email": student.email
#             # },
#             "registered_courses": [
#                 {
#                     "id": sc.course.id,
#                     "course_code": sc.course.course_code,
#                     "register_year": sc.register_year,
#                     "enrollment_date": sc.enrollment_date,
#                     "is_book_available": sc.is_book_available,
#                 }
#                 for sc in registered_courses
#             ]
#         }
#
#         return callback({"success": True, "data": data})
#
#     except Student.DoesNotExist:
#         return callback({"success": False, "message": "Student not found"})
#
# def make_book_reservation_service(sender, uuid, callback, **kwargs):
#     """
#     Get the student and their registered courses based on CustomUser UUID.
#     """
#     try:
#         # 1️⃣ Get the CustomUser using UUID
#         user = CustomUser.objects.get(uuid=uuid)
#         student = Student.objects.get(email=user.user.email)
#         student_course = StudentCourse.objects.filter(student__email=student.email)
#         data = [user, student, student_course]
#
#         return callback({"success": True, "data": str(data)})
#
#     except Exception as e:
#         return callback({"success": False, "message": str(e)})

def make_book_reservation_service(sender, uuid, callback, **kwargs):
    """
    Get student details and registered courses based on CustomUser UUID.
    """
    try:
        # 1️⃣ Get CustomUser
        user = CustomUser.objects.get(uuid=uuid)

        # 2️⃣ Get Student using email
        student = Student.objects.get(email=user.user.email)

        # 3️⃣ Get student courses
        student_courses = StudentCourse.objects.filter(
            student=student
        ).select_related("course")

        # 4️⃣ Prepare response
        data = {
            "student": {
                "id": student.id,
                "student_name": student.student_name,
                "reg_no": student.reg_no,
                "email": student.email,
                "nic": student.nic,
            },
            "courses": [
                {
                    "course_id": sc.course.id,
                    "course_name": sc.course.name,
                    "course_code": sc.course.course_code,

                    "register_year": sc.register_year,
                    "enrollment_date": sc.enrollment_date,
                    "expires_at": sc.expires_at,
                    "grade": sc.grade,

                    "is_active": sc.is_active,
                    "is_book_available": sc.is_book_available
                }
                for sc in student_courses
            ]
        }

        return callback({
            "success": True,
            "data": data
        })

    except CustomUser.DoesNotExist:
        return callback({"success": False, "message": "User not found"})

    except Student.DoesNotExist:
        return callback({"success": False, "message": "Student not found"})

    except Exception as e:
        return callback({"success": False, "message": str(e)})
