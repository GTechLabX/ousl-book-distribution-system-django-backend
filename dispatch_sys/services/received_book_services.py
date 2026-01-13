from dispatch_sys.models import ReceivedBook
from dispatch_sys.serializers.received_book_serializers import ReceivedBookSerializer


def received_book_add_service(sender, data, callback, **kwargs):
    serializer = ReceivedBookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({"success": True, "message": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def received_book_all_service(sender, callback, **kwargs):
    items = ReceivedBook.objects.all()
    serializer = ReceivedBookSerializer(items, many=True)
    return callback({"success": True, "data": serializer.data})


def received_book_show_service(sender, callback, pk, **kwargs):
    try:
        item = ReceivedBook.objects.get(pk=pk)
        serializer = ReceivedBookSerializer(item)
        return callback({"success": True, "data": serializer.data})
    except ReceivedBook.DoesNotExist:
        return callback({"success": False, "errors": "ReceivedBook not found"})


def received_book_update_service(sender, data, callback, pk, **kwargs):
    try:
        item = ReceivedBook.objects.get(pk=pk)
        serializer = ReceivedBookSerializer(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return callback({"success": True, "data": serializer.data})
        return callback({"success": False, "errors": serializer.errors})
    except ReceivedBook.DoesNotExist:
        return callback({"success": False, "errors": "ReceivedBook not found"})


def received_book_delete_service(sender, callback, pk, **kwargs):
    try:
        item = ReceivedBook.objects.get(pk=pk)
        data = ReceivedBookSerializer(item).data
        item.delete()
        return callback({"success": True, "message": "ReceivedBook deleted", "data": data})
    except ReceivedBook.DoesNotExist:
        return callback({"success": False, "errors": "ReceivedBook not found"})
