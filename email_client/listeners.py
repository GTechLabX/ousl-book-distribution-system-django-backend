from django.dispatch import receiver

from email_client.services.book_issue_service import send_book_issued_email_service
from email_client.services.send_staff_account_created_email_service import send_staff_account_created_email
from email_client.services.student_acc_reg_email_service import send_student_account_created_email
# from events.signals.emails_signals.book_issue_signals import book_issue_required
from events.signals.student_acc_created_signals import student_acc_created_required, staff_acc_created_required, \
    book_issue_required


@receiver(student_acc_created_required)
def handle_student_account_created(sender, username, email, password, img_path, **kwargs):
    try:
        send_student_account_created_email(
            to_email=email,
            username=username,
            password=password,
            img_path=img_path
        )
    except Exception as e:
        # log error, but DO NOT break registration
        print("Email sending failed:", str(e))


@receiver(staff_acc_created_required)
def handle_staff_account_created(sender, username, email, password, **kwargs):
    try:
        send_staff_account_created_email(
            to_email=email,
            username=username,
            password=password
        )
    except Exception as e:
        print("Email sending failed:", str(e))


@receiver(book_issue_required)
def handle_book_issued(sender, student_id, student_name, email, book_name, course_code, center_name, issue_date, issue_time, **kwargs):
    """
    Signal listener for book issuance.
    Calls your email function to notify the student.
    """
    try:
        send_book_issued_email_service(
            student_id=student_id,
            student_name=student_name,
            email=email,
            book_name=book_name,
            course_code=course_code,
            center_name=center_name,
            issue_date=issue_date,
            issue_time=issue_time
        )
    except Exception as e:
        print(f"Book issuance email sending failed for student {student_name}: {str(e)}")