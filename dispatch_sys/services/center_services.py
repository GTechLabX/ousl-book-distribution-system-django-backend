from dispatch_sys.models import Center
from dispatch_sys.serializers.center_serializers import CenterSerializer


def center_add_service(sender, data, callback, **kwargs):
    serializer = CenterSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def center_all_service(sender, callback, **kwargs):
    centers = Center.objects.all()
    serializer = CenterSerializer(centers, many=True)
    return callback({"success": True, "data": serializer.data})


def center_show_service(sender, callback, pk, **kwargs):
    try:
        center = Center.objects.get(pk=pk)
        serializer = CenterSerializer(center)
        return callback({"success": True, "data": serializer.data})
    except Center.DoesNotExist:
        return callback({"success": False, "errors": "Center does not exist"})


def center_update_service(sender, data, callback, pk, **kwargs):
    try:
        center = Center.objects.get(pk=pk)
        serializer = CenterSerializer(center, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({"success": True, "data": serializer.data})
    except Center.DoesNotExist:
        return callback({"success": False, "errors": "Center not found"})


def center_delete_service(sender, callback, pk, **kwargs):
    try:
        center = Center.objects.get(pk=pk)
        serializer = CenterSerializer(center)
        deleted_data = serializer.data
        center.delete()
        return callback({"success": True, "message": f"Center {pk} deleted", "data": deleted_data})
    except Center.DoesNotExist:
        return callback({"success": False, "errors": "Center not found"})
