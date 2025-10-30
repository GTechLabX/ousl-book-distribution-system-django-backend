from dispatch_sys.models import Faculty
from dispatch_sys.serializers.faculty_serializers import FacultySerializer


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
