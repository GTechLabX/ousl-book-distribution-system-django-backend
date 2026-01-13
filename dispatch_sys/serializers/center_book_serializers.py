from rest_framework import serializers
from dispatch_sys.models import CenterBook


class CenterBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterBook
        fields = "__all__"
