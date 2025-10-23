from rest_framework import serializers


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8)
    token = serializers.CharField()
    username = serializers.CharField()
