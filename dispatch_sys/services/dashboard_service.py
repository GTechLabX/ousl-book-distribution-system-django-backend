from django.db.models import Sum

from auth_sys.models import CustomUser, UserProfile
from dispatch_sys.models import Student, BookReservation, Book, ReceivedBook, CenterBook


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


def dashboard_center_service(sender, callback, uuid, **kwargs):
    try:

        user = CustomUser.objects.get(uuid=uuid)
        profile = user.userprofile
        center = profile.center_id

        if not center:
            callback({
                "success": False,
                "error": "Center not assigned to this user"
            })
            return

        register_student_count = Student.objects.filter(
            center=center
        ).count()

        active_reservation_count = BookReservation.objects.filter(
            center=center,
            is_active=True
        ).count()

        total_book_issued = ReceivedBook.objects.filter(
            center_book__center=center,
            is_received=True
        ).count()

        available_book_count = CenterBook.objects.filter(
            center_id=center,
            approved=True
        ).aggregate(
            total_allocated=Sum("allocation_quantity")
        )["total_allocated"] or 0

        latest_received_books = ReceivedBook.objects.filter(
            center_book__center=center
        ).select_related(
            "center_book",
            "center_book__books",
            "student"
        ).order_by("-id")[:5]

        latest_books = []

        for book in latest_received_books:
            latest_books.append({
                "id": book.id,
                "book": book.center_book.books.name,
                "student": book.student.student_name,
                "is_received": book.is_received
            })

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

    except Exception as e:
        callback({
            "success": False,
            "error": str(e)
        })
