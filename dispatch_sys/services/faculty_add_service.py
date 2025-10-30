from dispatch_sys.serializers.faculty_serializers import FacultySerializer


def faculty_add_service(sender, data, callback, **kwargs):
    serializer = FacultySerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        callback(
            {
                "success": True,
                "message": serializer.data
             }
        )
    return callback(
        {
            "success":False,
            "errors": serializer.errors
        }
    )
