from django.contrib.auth.models import User
from auth_sys.serializers.user_serializers import UserSerializer


def user_add_service(sender, data, callback, **kwargs):
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def user_update_service(sender, data, callback, pk, **kwargs):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return callback({"success": True, "data": serializer.data})
        return callback({"success": False, "errors": serializer.errors})
    except User.DoesNotExist:
        return callback({"success": False, "error": "User not found"})


def user_delete_service(sender, callback, pk, **kwargs):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return callback({"success": True, "message": "User deleted successfully"})
    except User.DoesNotExist:
        return callback({"success": False, "error": "User not found"})


def user_show_service(sender, callback, pk, **kwargs):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return callback({"success": True, "data": serializer.data})
    except User.DoesNotExist:
        return callback({"success": False, "error": "User not found"})


def user_all_service(sender, callback, **kwargs):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return callback({"success": True, "data": serializer.data})
