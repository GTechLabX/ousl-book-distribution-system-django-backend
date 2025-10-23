from dispatch_sys.models import Student
from dispatch_sys.serializers.student_reg_serializers import StudentSerializer


def student_all_service(sender, data, callback, **kwargs):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return callback(
        {
            "success": True,
            "message": serializer.data
        }
    )

