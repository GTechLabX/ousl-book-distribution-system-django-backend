from dispatch_sys.models import Student
from dispatch_sys.serializers.student_reg_serializers import StudentSerializer


def student_update_service(sender, data, callback, pk, **kwargs):
    print(data, pk)
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return callback({
            "success": False,
            "errors": f"Student with id {pk} does not exist"
        })

    serializer = StudentSerializer(student, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return callback({
            "success": True,
            "message": serializer.data,
        })
    else:
        return callback({
            "success": False,
            "errors": serializer.errors
        })
