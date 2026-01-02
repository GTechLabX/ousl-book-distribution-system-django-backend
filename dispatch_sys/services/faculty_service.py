from dispatch_sys.models import Faculty
from dispatch_sys.serializers.faculty_serializers import FacultySerializer


def faculty_add_service(data, callback, **kwargs):
    serializer = FacultySerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return callback({
            "success": True,
            "message": serializer.data
        })

    return callback({
        "success": False,
        "errors": serializer.errors
    })


def faculty_all_service(sender, callback, **kwargs):
    faculties = Faculty.objects.all()
    serializer = FacultySerializer(data=faculties)
    if serializer.is_valid(raise_exception=True):
        return callback(
            {
                "success": True,
                "data": serializer.data
            }
        )

    return callback(
        {
            "success": False,
            "errors": serializer.errors
        }
    )


def faculty_delete_service(sender, callback, pk, **kwargs):
    try:
        faculty = Faculty.objects.get(pk=pk)

        # serialize data before deletion to return it
        serializer = FacultySerializer(instance=faculty)
        deleted_data = serializer.data

        # Delete the object
        faculty.delete()

        return callback({
            "success": True,
            "message": f"Faculty with id {pk} has been deleted",
            "data": deleted_data
        })

    except Faculty.DoesNotExist:
        return callback({
            "success": False,
            "errors": f"Faculty with id {pk} does not exist"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })


def faculty_update_service(sender, data, callback, pk, **kwargs):
    try:
        faculty = Faculty.objects.get(pk=pk)
        serializer = FacultySerializer(instance=faculty, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({
                "success": True,
                "data": serializer.data
            })

    except Faculty.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Faculty not found"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })


def faculty_show_service(sender, callback, pk, **kwargs):
    try:
        faculty = Faculty.objects.get(pk=pk)
        serializer = FacultySerializer(instance=faculty)
        return callback({
            "success": True,
            "data": serializer.data
        })

    except Faculty.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Faculty does not exist"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })
