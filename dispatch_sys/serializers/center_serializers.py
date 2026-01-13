from rest_framework import serializers
from dispatch_sys.models import Center


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = "__all__"
