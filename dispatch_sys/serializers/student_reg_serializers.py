from rest_framework import serializers
from dispatch_sys.models import Student


from rest_framework import serializers
from dispatch_sys.models import Student


class StudentSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source="district.district_name", read_only=True)
    center_name = serializers.CharField(source="center.c_name", read_only=True)
    degree_program_name = serializers.CharField(source="degree_program.d_program", read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "student_name",
            "nic",
            "s_no",
            "reg_no",
            "email",
            "district",
            "district_name",
            "center",
            "center_name",
            "degree_program",
            "degree_program_name",
        ]
