from dispatch_sys.serializers.student_reg_serializers import StudentSerializer


def register_student(data):
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        student = serializer.save()
        return {"success": True, "student_id": student.id}
    return {"success": False, "errors": serializer.errors}

