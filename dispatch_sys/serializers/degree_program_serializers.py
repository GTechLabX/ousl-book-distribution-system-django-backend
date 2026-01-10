from rest_framework import serializers
from dispatch_sys.models import DegreeProgram


class DegreeProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeProgram
        fields = [
            "id",
            "d_program",
            "info",
            "department",
            "student"
        ]
