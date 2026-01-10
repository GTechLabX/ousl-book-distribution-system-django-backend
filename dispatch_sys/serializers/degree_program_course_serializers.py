from rest_framework import serializers
from dispatch_sys.models import DegreeProgramCourse


class DegreeProgramCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeProgramCourse
        fields = "__all__"
