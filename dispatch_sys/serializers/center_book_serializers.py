from rest_framework import serializers
from dispatch_sys.models import CenterBook


class CenterBookSerializer(serializers.ModelSerializer):
    # Works for the UI expecting just the name
    book_name = serializers.CharField(source="books.name", read_only=True)

    # Works for the UI expecting the center name
    center_name = serializers.CharField(source="center.c_name", read_only=True)

    # Works for the UI expecting "Name (Course Code)"
    book_with_course = serializers.SerializerMethodField()

    class Meta:
        model = CenterBook
        fields = [
            "id",
            "center",
            "center_name",
            "books",
            "book_name",  # <--- UI A uses this
            "book_with_course",  # <--- UI B uses this
            "date",
            "time",
            "status",
            "approved",
            "allocation_quantity",
        ]

    def get_book_with_course(self, obj):
        try:
            # Safely handle if books or course are missing
            return f"{obj.books.name} ({obj.books.course.course_code})"
        except AttributeError:
            return "N/A"