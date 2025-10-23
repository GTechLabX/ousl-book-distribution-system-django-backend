from dispatch_sys.models import Student
from dispatch_sys.serializers.student_reg_serializers import StudentSerializer


def student_service(sender, data, callback, pk, **kwargs):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return callback(
            {
                "success": False,
                "errors": str(e)
            }
        )
    serializer = StudentSerializer(student)

    return callback(
        {
            "success": True,
            "message": serializer.data
        }
    )

