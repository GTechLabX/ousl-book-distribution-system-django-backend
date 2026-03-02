# from django.contrib.auth.models import User
# from auth_sys.serializers.user_serializers import UserSerializer
#
#
#
# def user_update_service(sender, data, callback, pk, **kwargs):
#     try:
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return callback({"success": True, "data": serializer.data})
#         return callback({"success": False, "errors": serializer.errors})
#     except User.DoesNotExist:
#         return callback({"success": False, "error": "User not found"})
#
#
# def user_delete_service(sender, callback, pk, **kwargs):
#     try:
#         user = User.objects.get(pk=pk)
#         user.delete()
#         return callback({"success": True, "message": "User deleted successfully"})
#     except User.DoesNotExist:
#         return callback({"success": False, "error": "User not found"})
#
#
# def user_show_service(sender, callback, pk, **kwargs):
#     try:
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user)
#         return callback({"success": True, "data": serializer.data})
#     except User.DoesNotExist:
#         return callback({"success": False, "error": "User not found"})
#
#
# def user_all_service(sender, callback, **kwargs):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return callback({"success": True, "data": serializer.data})


from django.contrib.auth.models import User
from django.db import transaction
from auth_sys.models import CustomUser, UserProfile
from auth_sys.serializers.user_serializers import FullUserSerializer, UserProfileSerializer, CustomUserSerializer, \
    DjangoUserSerializer


def user_show_service(sender, callback, user_id, **kwargs):
    if not user_id:
        return callback({"success": False, "error": "user_id is required"})

    try:
        user = User.objects.select_related("customuser", "customuser__userprofile").get(id=user_id)
        custom_user = user.customuser
        profile = custom_user.userprofile

        serializer = FullUserSerializer({
            "user": user,
            "custom_user": custom_user,
            "profile": profile,
        })

        callback({"success": True, "data": serializer.data})

    except User.DoesNotExist:
        callback({"success": False, "error": "User not found"})


def user_add_service(sender, data, callback, **kwargs):
    serializer = DjangoUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


# def user_add_service(sender, data, callback, **kwargs):
#     try:
#         with transaction.atomic():
#
#             # 1️⃣ Create Django User
#             user_data = data.get("user")
#             user = User.objects.create_user(**user_data)
#
#             # 2️⃣ Create CustomUser
#             custom_data = data.get("custom_user")
#             custom_user = CustomUser.objects.create(user=user, **custom_data)
#
#             # 3️⃣ Create User Profile
#             profile_data = data.get("profile", {})
#             UserProfile.objects.create(user=custom_user, **profile_data)
#
#             callback({
#                 "success": True,
#                 "message": "User created successfully"
#             })
#
#     except Exception as e:
#         callback({
#             "success": False,
#             "error": str(e)
#         })


def user_update_service(sender, data, callback, user_id=None, **kwargs):
    try:
        with transaction.atomic():

            user = User.objects.get(id=user_id)
            custom_user = user.customuser
            profile = custom_user.userprofile

            # Update Django User
            DjangoUserSerializer(
                user,
                data=data.get("user", {}),
                partial=True
            ).is_valid(raise_exception=True)

            DjangoUserSerializer(
                user,
                data=data.get("user", {}),
                partial=True
            ).save()

            # Update CustomUser
            CustomUserSerializer(
                custom_user,
                data=data.get("custom_user", {}),
                partial=True
            ).is_valid(raise_exception=True)

            CustomUserSerializer(
                custom_user,
                data=data.get("custom_user", {}),
                partial=True
            ).save()

            # Update Profile
            UserProfileSerializer(
                profile,
                data=data.get("profile", {}),
                partial=True
            ).is_valid(raise_exception=True)

            UserProfileSerializer(
                profile,
                data=data.get("profile", {}),
                partial=True
            ).save()

            callback({
                "success": True,
                "message": "User updated successfully"
            })

    except Exception as e:
        callback({
            "success": False,
            "error": str(e)
        })


def user_delete_service(sender, callback, user_id=None, **kwargs):
    try:
        user = User.objects.get(id=user_id)
        user.delete()  # cascades to CustomUser & UserProfile

        callback({
            "success": True,
            "message": "User deleted successfully"
        })

    except User.DoesNotExist:
        callback({
            "success": False,
            "error": "User not found"
        })


def user_all_service(sender, callback, **kwargs):
    users = User.objects.all().select_related()

    data = []

    for user in users:
        try:
            custom_user = user.customuser
            profile = custom_user.userprofile

            serializer = FullUserSerializer({
                "user": user,
                "custom_user": custom_user,
                "profile": profile,
            })

            data.append(serializer.data)

        except Exception:
            continue

    callback({
        "success": True,
        "data": data
    })
