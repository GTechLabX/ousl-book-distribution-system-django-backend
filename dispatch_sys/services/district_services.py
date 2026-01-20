from dispatch_sys.models import District
from dispatch_sys.serializers.district_serializers import DistrictSerializer


def district_add_service(sender, data, callback, **kwargs):
    serializer = DistrictSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def district_update_service(sender, data, pk, callback, **kwargs):
    try:
        district = District.objects.get(pk=pk)
        serializer = DistrictSerializer(district, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return callback({"success": True, "data": serializer.data})
        return callback({"success": False, "errors": serializer.errors})
    except District.DoesNotExist:
        return callback({"success": False, "errors": "District not found"})


def district_delete_service(sender, pk, callback, **kwargs):
    try:
        district = District.objects.get(pk=pk)
        data = DistrictSerializer(district).data
        district.delete()
        return callback({"success": True, "message": "District deleted", "data": data})
    except District.DoesNotExist:
        return callback({"success": False, "errors": "District not found"})


def district_show_service(sender, pk, callback, **kwargs):
    try:
        district = District.objects.get(pk=pk)
        serializer = DistrictSerializer(district)
        return callback({"success": True, "data": serializer.data})
    except District.DoesNotExist:
        return callback({"success": False, "errors": "District not found"})


def district_all_service(sender, callback, **kwargs):
    districts = District.objects.all()
    serializer = DistrictSerializer(districts, many=True)
    return callback({"success": True, "data": serializer.data})
