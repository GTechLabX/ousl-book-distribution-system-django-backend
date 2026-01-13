from django.dispatch import receiver
from email_client.services.student_acc_reg_email_service import send_student_account_created_email
from events.signals.student_acc_created_signals import student_acc_created_required


@receiver(student_acc_created_required)
def handle_student_account_created(sender, username, email, password, **kwargs):
    send_student_account_created_email(
        to_email=email,
        username=username,
        password=password
    )
