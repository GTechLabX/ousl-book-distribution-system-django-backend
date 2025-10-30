from dispatch_sys.models import Faculty
from dispatch_sys.serializers.faculty_serializers import FacultySerializer


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
