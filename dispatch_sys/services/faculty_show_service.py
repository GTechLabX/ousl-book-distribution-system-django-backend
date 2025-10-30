from dispatch_sys.models import Faculty
from dispatch_sys.serializers.faculty_serializers import FacultySerializer


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
