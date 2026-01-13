from dispatch_sys.models import CenterBook
from dispatch_sys.serializers.center_book_serializers import CenterBookSerializer


def center_book_add_service(sender, data, callback, **kwargs):
    serializer = CenterBookSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return callback({
            "success": True,
            "message": serializer.data
        })

    return callback({
        "success": False,
        "errors": serializer.errors
    })


def center_book_all_service(sender, callback, **kwargs):
    center_books = CenterBook.objects.all()
    serializer = CenterBookSerializer(center_books, many=True)

    return callback({
        "success": True,
        "data": serializer.data
    })


def center_book_show_service(sender, callback, pk, **kwargs):
    try:
        center_book = CenterBook.objects.get(pk=pk)
        serializer = CenterBookSerializer(center_book)

        return callback({
            "success": True,
            "data": serializer.data
        })

    except CenterBook.DoesNotExist:
        return callback({
            "success": False,
            "errors": "CenterBook not found"
        })


def center_book_update_service(sender, data, callback, pk, **kwargs):
    try:
        center_book = CenterBook.objects.get(pk=pk)
        serializer = CenterBookSerializer(
            instance=center_book,
            data=data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return callback({
                "success": True,
                "data": serializer.data
            })

        return callback({
            "success": False,
            "errors": serializer.errors
        })

    except CenterBook.DoesNotExist:
        return callback({
            "success": False,
            "errors": "CenterBook not found"
        })


def center_book_delete_service(sender, callback, pk, **kwargs):
    try:
        center_book = CenterBook.objects.get(pk=pk)
        serializer = CenterBookSerializer(center_book)
        deleted_data = serializer.data

        center_book.delete()

        return callback({
            "success": True,
            "message": "CenterBook deleted successfully",
            "data": deleted_data
        })

    except CenterBook.DoesNotExist:
        return callback({
            "success": False,
            "errors": "CenterBook not found"
        })
