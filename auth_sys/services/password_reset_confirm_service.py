from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator

from auth_sys.serializers.password_reset_confirm_serializer import PasswordResetConfirmSerializer


def user_password_reset_confirm_service(sender, data, callback, **kwargs):
    serializer = PasswordResetConfirmSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data['username']
    token = serializer.validated_data['token']
    new_password = serializer.validated_data['new_password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return callback({
            "success": False,
            "error": "Invalid username",
        })

    if default_token_generator.check_token(user, token):
        user.set_password(new_password)
        user.save()
        return callback({
            "success": True,
            "message": "Password has been reset successfully"
        })
    else:
        return callback({
            "success": False,
            "error": "Invalid or expired token"
        })
