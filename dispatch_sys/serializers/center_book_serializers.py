from rest_framework import serializers
from dispatch_sys.models import CenterBook

class CenterBookSerializer(serializers.ModelSerializer):
    center_name = serializers.CharField(source="center.c_name", read_only=True)
    # Combine book name + course code
    book_with_course = serializers.SerializerMethodField()

    class Meta:
        model = CenterBook
        fields = [
            "id",
            "center",
            "center_name",
            "books",
            "book_with_course",
            "date",
            "time",
            "status",
            "approved",
            "allocation_quantity",
        ]

    def get_book_with_course(self, obj):
        # obj.books is the Book instance
        # obj.books.course is the Course instance
        return f"{obj.books.name} ({obj.books.course.course_code})"
