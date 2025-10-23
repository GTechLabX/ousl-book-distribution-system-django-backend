from dispatch_sys.models import Student
from dispatch_sys.serializers.student_reg_serializers import StudentSerializer


def student_delete_service(sender, callback, pk, **kwargs):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return callback({
            "success": False,
            "errors": f"Student with id {pk} does not exist"
        })

    # Optional: serialize before deletion if you want to return data
    serializer = StudentSerializer(student)
    student.delete()  # deletes the record

    return callback({
        "success": True,
        "message": "Student deleted successfully",
        "deleted_student": serializer.data  # returns deleted data
    })
