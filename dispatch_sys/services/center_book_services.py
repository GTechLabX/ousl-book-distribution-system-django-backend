from django.db import transaction

from dispatch_sys.models import CenterBook, Book
from dispatch_sys.serializers.center_book_serializers import CenterBookSerializer


def center_book_add_service(sender, data, callback, **kwargs):
    serializer = CenterBookSerializer(data=data)

    if not serializer.is_valid():
        return callback({
            "success": False,
            "errors": serializer.errors
        })

    try:
        with transaction.atomic():
            book_id = serializer.validated_data["books"].id
            allocation_qty = serializer.validated_data["allocation_quantity"]

            # Lock the book row (important for concurrency)
            book = Book.objects.select_for_update().get(id=book_id)

            # 1️⃣ Check stock
            if book.left_quantity < allocation_qty:
                return callback({
                    "success": False,
                    "errors": {
                        "stock": "Not enough books in stock"
                    }
                })

            # 2️⃣ Reduce stock
            book.left_quantity -= allocation_qty
            book.save()

            # 3️⃣ Save CenterBook record
            center_book = serializer.save()

            return callback({
                "success": True,
                "message": CenterBookSerializer(center_book).data
            })

    except Book.DoesNotExist:
        return callback({
            "success": False,
            "errors": {
                "book": "Book not found"
            }
        })



def center_book_all_service(sender, callback, **kwargs):
    center_books = CenterBook.objects.select_related("center", "books")
    serializer = CenterBookSerializer(center_books, many=True)

    return callback({
        "success": True,
        "data": serializer.data
    })


def center_book_show_service(sender, callback, pk, **kwargs):
    try:
        center_book = CenterBook.objects.get(pk=pk)
        serializer = CenterBookSerializer(center_book)

        course_code = center_book.books.course.course_code

        return callback({
            "success": True,
            "data": serializer.data,
            "course_code": course_code
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
