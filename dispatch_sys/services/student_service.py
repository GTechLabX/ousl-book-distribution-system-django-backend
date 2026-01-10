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


def register_student(sender, data, callback, **kwargs):
    serializer = StudentSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        student = serializer.save()
        return callback(
            {"success": True, "student_id": student.id}
        )
    return callback(
        {"success": False, "errors": serializer.errors}
    )


def student_delete_service(sender, callback, pk, **kwargs):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return callback({
            "success": False,
            "errors": f"Student with id {pk} does not exist"
        })

    # serialize before deletion if you want to return data
    serializer = StudentSerializer(student)
    student.delete()  # deletes the record

    return callback({
        "success": True,
        "message": "Student deleted successfully",
        "deleted_student": serializer.data  # returns deleted data
    })


def student_all_service(sender, callback, **kwargs):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return callback(
        {
            "success": True,
            "message": serializer.data
        }
    )


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
