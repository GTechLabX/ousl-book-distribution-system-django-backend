from dispatch_sys.models import Student, DegreeProgramCourse, StudentCourse
from pyzbar.pyzbar import decode
from PIL import Image


def get_student_from_qr_service(qr_image_file, **kwargs):
    """
    Decode QR image and return a result dict suitable for callback.
    """
    try:
        img = Image.open(qr_image_file)
    except Exception:
        return {"success": False, "error": "Invalid image"}

    decoded_objects = decode(img)
    if not decoded_objects:
        return {"success": False, "error": "No QR code detected"}

    for obj in decoded_objects:
        qr_data = obj.data.decode("utf-8").strip()
        print("QR content:", repr(qr_data))

        # Check for "INC-ID:" format
        if "INC-ID:" in qr_data:
            student_id_str = qr_data.split("INC-ID:")[1].split(",")[0].strip()
        else:
            # Skip other QR formats
            continue

        # Fetch student from DB
        print(student_id_str)

        try:
            # Get the student
            student = Student.objects.get(nic=student_id_str)

            # Get all courses the student has enrolled in
            enrolled_courses = StudentCourse.objects.filter(
                student=student
            ).select_related('course')

            # Prepare the data
            courses_data = [
                {
                    "id": sc.course.id,
                    "course_code": sc.course.course_code,
                    "name": sc.course.name,
                    "register_year": sc.register_year,
                    "enrollment_date": sc.enrollment_date,
                    "grade": sc.grade,
                    "is_active": sc.is_active,
                    "expires_at": sc.expires_at
                }
                for sc in enrolled_courses
            ]

            return {
                "success": True,
                "student": {
                    "id": student.id,
                    "student_name": student.student_name,
                    "email": student.email,
                    "degree_program": student.degree_program.d_program,
                    "enrolled_courses": courses_data
                }
            }

        except Student.DoesNotExist:
            return {
                "success": False,
                "error": "Student not found"
            }

    # If loop ends with no valid QR found
    return {"success": False, "error": "Invalid QR code format"}
