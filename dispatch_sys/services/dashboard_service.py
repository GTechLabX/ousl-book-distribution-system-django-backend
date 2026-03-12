
from django.db.models import Sum
from dispatch_sys.models import Student, BookReservation, Book, ReceivedBook

def dashboard_service(sender, callback, **kwargs):

    # Count students, reservations, received books
    register_student_count = Student.objects.count()
    active_reservation_count = BookReservation.objects.count()
    total_book_issued = ReceivedBook.objects.filter(is_received=True).count()

    # Sum all left_quantity of all books
    available_book_count = Book.objects.aggregate(total_left=Sum('left_quantity'))['total_left'] or 0

    # Get latest 5 received books
    latest_received_books = ReceivedBook.objects.order_by('-id')[:5]

    latest_books = []
    for book in latest_received_books:
        latest_books.append({
            "id": book.id,
            "book": str(book.center_book.books.name),
            "student": str(book.student),
            "is_received": book.is_received
        })

    # Prepare response data
    data = {
        "success": True,
        "data": {
            "register_student_count": register_student_count,
            "active_reservation_count": active_reservation_count,
            "available_book_count": available_book_count,
            "total_book_issued": total_book_issued,
            "latest_received_books": latest_books
        }
    }

    callback(data)
