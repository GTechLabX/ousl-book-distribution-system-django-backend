from rest_framework import serializers
from dispatch_sys.models import BookReservation


class BookReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReservation
        fields = "__all__"
