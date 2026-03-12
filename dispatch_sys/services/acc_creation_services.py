from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.exceptions import ValidationError

from auth_sys.models import CustomUser


def create_staff_service(sender, data, callback, **kwargs):
    try:
        with transaction.atomic():

            username = data.get("username")
            email = data.get("email")
            role = data.get("role")

            password = username

            # --- Check existing user ---
            if User.objects.filter(username=username).exists():
                raise ValidationError("User already exists")

            # --- Create Django User ---
            django_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # --- Create CustomUser ---
            custom_user, _ = CustomUser.objects.get_or_create(user=django_user)
            custom_user.role = role
            custom_user.save()

            return callback({
                "success": True,
                "message": "Account created successfully",
                "user_id": django_user.id
            })

    except Exception as e:
        return callback({
            "success": False,
            "error": str(e)
        })
