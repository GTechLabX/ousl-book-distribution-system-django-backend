from dispatch_sys.models import Student
from pyzbar.pyzbar import decode
from PIL import Image


def get_student_from_qr_service(qr_image_file):
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
        qr_data = obj.data.decode("utf-8")
        if qr_data.startswith("STU-"):
            student_id = int(qr_data.split("-")[1])
            try:
                student = Student.objects.get(id=student_id)
                return {
                    "success": True,
                    "student": {
                        "id": student.id,
                        "student_name": student.student_name,
                        "email": student.email
                    }
                }
            except Student.DoesNotExist:
                return {"success": False, "error": "Student not found"}

    return {"success": False, "error": "Invalid QR code format"}
