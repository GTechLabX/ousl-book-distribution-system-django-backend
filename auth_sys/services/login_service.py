from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from auth_sys.models import CustomUser  # make sure to import your CustomUser model

def login_service(sender, data, callback, **kwargs):
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return callback({
            "success": False,
            "message": "Username and password are required."
        })

    user = authenticate(username=username, password=password)

    if user:
        try:
            # Get the admin's CustomUser record
            custom_user = CustomUser.objects.get(user=user)
        except CustomUser.DoesNotExist:
            return callback({
                "success": False,
                "message": "CustomUser record not found for this user."
            })

        refresh = RefreshToken.for_user(user)

        return callback({
            "success": True,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "role": custom_user.role,      # get role from CustomUser
            "uuid": str(custom_user.uuid), # get UUID from CustomUser
        })

    else:
        return callback({
            "success": False,
            "message": "Invalid credentials."
        })
