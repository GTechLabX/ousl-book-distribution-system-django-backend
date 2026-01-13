from rest_framework import serializers
from dispatch_sys.models import ReceivedBook


class ReceivedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedBook
        fields = "__all__"
