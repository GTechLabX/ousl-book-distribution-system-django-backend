from django.contrib.auth.models import User
from rest_framework import serializers
from auth_sys.models import UserProfile, CustomUser


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = (
#             "id",
#             "username",
#             "email",
#             "first_name",
#             "last_name",
#             "password",
#             "is_active",
#             "is_staff",
#             "is_superuser",
#         )
#
#     def create(self, validated_data):
#         password = validated_data.pop("password")
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user
#
#


class DjangoUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        )

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class CustomUserSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = CustomUser
        fields = (
            "uuid",
            "dob",
            "gender",
            "picture_path",
            "phone_no",
            "role",
            "user",
        )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class FullUserSerializer(serializers.Serializer):
    user = DjangoUserSerializer()
    custom_user = CustomUserSerializer()
    profile = UserProfileSerializer()
