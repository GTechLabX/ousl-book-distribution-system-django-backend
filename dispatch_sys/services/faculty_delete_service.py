from dispatch_sys.models import Faculty
from dispatch_sys.serializers.faculty_serializers import FacultySerializer


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
