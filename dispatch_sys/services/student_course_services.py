from dispatch_sys.models import StudentCourse
from dispatch_sys.serializers.student_course_serializers import StudentCourseSerializer


def student_course_add_service(sender, data, callback, **kwargs):
    serializer = StudentCourseSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def student_course_all_service(sender, callback, **kwargs):
    items = StudentCourse.objects.all()
    serializer = StudentCourseSerializer(items, many=True)
    return callback({"success": True, "data": serializer.data})


def student_course_show_service(sender, callback, pk, **kwargs):
    try:
        item = StudentCourse.objects.get(pk=pk)
        serializer = StudentCourseSerializer(item)
        return callback({"success": True, "data": serializer.data})
    except StudentCourse.DoesNotExist:
        return callback({"success": False, "errors": "StudentCourse does not exist"})


def student_course_update_service(sender, data, callback, pk, **kwargs):
    try:
        item = StudentCourse.objects.get(pk=pk)
        serializer = StudentCourseSerializer(item, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({"success": True, "data": serializer.data})
    except StudentCourse.DoesNotExist:
        return callback({"success": False, "errors": "StudentCourse not found"})


def student_course_delete_service(sender, callback, pk, **kwargs):
    try:
        item = StudentCourse.objects.get(pk=pk)
        serializer = StudentCourseSerializer(item)
        deleted_data = serializer.data
        item.delete()
        return callback({
            "success": True,
            "message": f"StudentCourse {pk} deleted",
            "data": deleted_data
        })
    except StudentCourse.DoesNotExist:
        return callback({"success": False, "errors": "StudentCourse not found"})
