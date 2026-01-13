from dispatch_sys.models import BookReservation
from dispatch_sys.serializers.book_reservation_serializer import BookReservationSerializer


def book_reservation_add_service(sender, data, callback, **kwargs):
    serializer = BookReservationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def book_reservation_update_service(sender, pk, data, callback, **kwargs):
    try:
        reservation = BookReservation.objects.get(pk=pk)
        serializer = BookReservationSerializer(reservation, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return callback({"success": True, "data": serializer.data})
        return callback({"success": False, "errors": serializer.errors})
    except BookReservation.DoesNotExist:
        return callback({"success": False, "message": "Reservation not found"})



def book_reservation_delete_service(sender, pk, callback, **kwargs):
    try:
        BookReservation.objects.get(pk=pk).delete()
        return callback({"success": True, "message": "Deleted successfully"})
    except BookReservation.DoesNotExist:
        return callback({"success": False, "message": "Reservation not found"})


def book_reservation_show_service(sender, pk, callback, **kwargs):
    try:
        reservation = BookReservation.objects.get(pk=pk)
        serializer = BookReservationSerializer(reservation)
        return callback({"success": True, "data": serializer.data})
    except BookReservation.DoesNotExist:
        return callback({"success": False, "message": "Reservation not found"})


def book_reservation_all_service(sender, callback, **kwargs):
    reservations = BookReservation.objects.all()
    serializer = BookReservationSerializer(reservations, many=True)
    return callback({"success": True, "data": serializer.data})


