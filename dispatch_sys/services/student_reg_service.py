from dispatch_sys.serializers.student_reg_serializers import StudentSerializer


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

