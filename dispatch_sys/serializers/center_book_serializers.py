from rest_framework import serializers
from dispatch_sys.models import CenterBook


class CenterBookSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source="books.name", read_only=True)
    center_name = serializers.CharField(source="center.c_name", read_only=True)

    class Meta:
        model = CenterBook
        fields = [
            "id",
            "center",
            "center_name",
            "books",
            "book_name",
            "date",
            "time",
            "status",
            "approved",
            "allocation_quantity",
        ]
