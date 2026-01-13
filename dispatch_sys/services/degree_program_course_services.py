from dispatch_sys.models import DegreeProgramCourse
from dispatch_sys.serializers.degree_program_course_serializers import (
    DegreeProgramCourseSerializer
)


def degree_program_course_add_service(sender, data, callback, **kwargs):
    serializer = DegreeProgramCourseSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return callback({
            "success": True,
            "data": serializer.data
        })


def degree_program_course_all_service(sender, callback, **kwargs):
    items = DegreeProgramCourse.objects.all()
    serializer = DegreeProgramCourseSerializer(items, many=True)

    return callback({
        "success": True,
        "data": serializer.data
    })


def degree_program_course_show_service(sender, callback, pk, **kwargs):
    try:
        item = DegreeProgramCourse.objects.get(pk=pk)
        serializer = DegreeProgramCourseSerializer(item)

        return callback({
            "success": True,
            "data": serializer.data
        })

    except DegreeProgramCourse.DoesNotExist:
        return callback({
            "success": False,
            "errors": "DegreeProgramCourse does not exist"
        })


def degree_program_course_update_service(sender, data, callback, pk, **kwargs):
    try:
        item = DegreeProgramCourse.objects.get(pk=pk)
        serializer = DegreeProgramCourseSerializer(
            item,
            data=data,
            partial=True
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({
                "success": True,
                "data": serializer.data
            })

    except DegreeProgramCourse.DoesNotExist:
        return callback({
            "success": False,
            "errors": "DegreeProgramCourse not found"
        })


def degree_program_course_delete_service(sender, callback, pk, **kwargs):
    try:
        item = DegreeProgramCourse.objects.get(pk=pk)
        serializer = DegreeProgramCourseSerializer(item)
        deleted_data = serializer.data

        item.delete()

        return callback({
            "success": True,
            "message": f"DegreeProgramCourse {pk} deleted",
            "data": deleted_data
        })

    except DegreeProgramCourse.DoesNotExist:
        return callback({
            "success": False,
            "errors": "DegreeProgramCourse not found"
        })


