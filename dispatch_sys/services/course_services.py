from dispatch_sys.models import Course
from dispatch_sys.serializers.course_serializers import CourseSerializer


def course_add_service(sender, data, callback, **kwargs):
    serializer = CourseSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return callback({
            "success": True,
            "data": serializer.data
        })

def course_all_service(sender, callback, **kwargs):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)

    return callback({
        "success": True,
        "data": serializer.data
    })

def course_show_service(sender, callback, pk, **kwargs):
    try:
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)

        return callback({
            "success": True,
            "data": serializer.data
        })

    except Course.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Course does not exist"
        })


def course_update_service(sender, data, callback, pk, **kwargs):
    try:
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({
                "success": True,
                "data": serializer.data
            })

    except Course.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Course not found"
        })


def course_delete_service(sender, callback, pk, **kwargs):
    try:
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        deleted_data = serializer.data

        course.delete()

        return callback({
            "success": True,
            "message": f"Course {pk} deleted",
            "data": deleted_data
        })

    except Course.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Course not found"
        })
