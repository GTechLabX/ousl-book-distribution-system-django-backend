from django.dispatch import receiver
from events.signals import student_registration_requested
from services.student_service import register_student


@receiver(student_registration_requested)
def handle_student_registration(sender, data, callback, **kwargs):
    # send the data the student reg function
    result = register_student(sender=sender, data=data, callback=callback)
    callback(result)
