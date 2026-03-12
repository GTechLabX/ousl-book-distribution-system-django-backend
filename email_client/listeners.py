from django.dispatch import receiver

from email_client.services.book_issue_service import send_book_issue_email
from email_client.services.student_acc_reg_email_service import send_student_account_created_email
from events.signals.emails_signals.book_issue_signals import book_issue_required
from events.signals.student_acc_created_signals import student_acc_created_required


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


@receiver(book_issue_required)
def handle_book_issue(sender, student, course, **kwargs):
    try:
        send_book_issue_email(
            to_email=student.email,
            student_name=student.student_name,
            course_code=course.course.course_code,
            course_name=course.course.name,
            register_year=course.register_year
        )
    except Exception as e:
        # Do NOT break issuing process
        print("Book issue email failed:", str(e))
