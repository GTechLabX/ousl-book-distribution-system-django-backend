from dispatch_sys.models import Book
from dispatch_sys.serializers.book_serializers import BookSerializer


def book_add_service(sender, data, callback, **kwargs):
    serializer = BookSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return callback({"success": True, "data": serializer.data})
    return callback({"success": False, "errors": serializer.errors})


def book_all_service(sender=None, callback=None, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    if callable(callback):
        return callback({"success": True, "data": serializer.data})

    return {"success": True, "data": serializer.data}


def book_show_service(sender, callback, pk, **kwargs):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book)
        return callback({
            "success": True,
            "data": serializer.data
        })

    except Book.DoesNotExist:
        return callback({
            "success": False,
            "errors": "Faculty does not exist"
        })

    except Exception as e:
        return callback({
            "success": False,
            "errors": str(e)
        })


def book_update_service(sender, data, callback, pk, **kwargs):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return callback({"success": True, "data": serializer.data})
    except Book.DoesNotExist:
        return callback({"success": False, "errors": "Book not found"})


def book_delete_service(sender, callback, pk, **kwargs):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        deleted_data = serializer.data
        book.delete()
        return callback({"success": True, "message": f"Book {pk} deleted", "data": deleted_data})
    except Book.DoesNotExist:
        return callback({"success": False, "errors": "Book not found"})
