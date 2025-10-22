from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


def login_service(sender, data, callback, **kwargs):
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        callback({
            "success": False,
            "message": "Username and password are required."
        })
        return

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        callback({
            "success": True,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username
        })
    else:
        callback({
            "success": False,
            "message": "Invalid credentials."
        })
