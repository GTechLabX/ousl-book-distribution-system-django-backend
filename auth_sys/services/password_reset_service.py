from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from auth_sys.serializers.password_reset_serializer import PasswordResetRequestSerializer


def user_password_reset_service(sender, data, callback, **kwargs):
    serializer = PasswordResetRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return callback({
            "success": False,
            "error": "User with this email does not exist",
        })

    # For production, send email with this token
    # send_mail("Reset Password", f"Your token: {token}", "from@example.com", [email])

    # generate token
    token = default_token_generator.make_token(user)

    return callback({
        "success": True,
        "message": "Password reset token generated",
        "token": token,
        "username": user.username
    })
