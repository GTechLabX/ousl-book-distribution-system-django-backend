from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from auth_sys.models import CustomUser, UserProfile
from events.signals.student_acc_created_signals import staff_acc_created_required


class DjangoUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This email is already registered."
            )
        ]
    )

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "password")


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("uuid", "dob", "gender", "picture_path", "phone_no", "role")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("center_id", "bio",)


class FullUserSerializer(serializers.Serializer):
    user = DjangoUserSerializer()
    custom_user = CustomUserSerializer()
    profile = UserProfileSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        custom_user_data = validated_data.pop("custom_user")
        profile_data = validated_data.pop("profile")

        with transaction.atomic():
            # 1. Create Django User
            password = user_data.pop("password")

            user = User(**user_data)
            user.set_password(password)
            user.save()

            # 2. Create CustomUser
            custom_user, _ = CustomUser.objects.update_or_create(
                user=user,
                defaults=custom_user_data
            )

            # 3. Create Profile
            profile, _ = UserProfile.objects.update_or_create(
                user=custom_user,
                defaults=profile_data
            )

            # 4. Send Email
            if custom_user.role in ["ADMIN2", "STAFF"]:
                staff_acc_created_required.send(
                    sender=self.__class__,
                    username=user.username,
                    email=user.email,
                    password=password,
                )

        return {
            "user": user,
            "custom_user": custom_user,
            "profile": profile
        }

    def to_representation(self, instance):
        return {
            "user": DjangoUserSerializer(instance["user"]).data,
            "custom_user": CustomUserSerializer(instance["custom_user"]).data,
            "profile": UserProfileSerializer(instance["profile"]).data,
        }
