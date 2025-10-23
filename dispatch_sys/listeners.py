from django.dispatch import receiver

from dispatch_sys.services.student_all_service import student_all_service
from dispatch_sys.services.student_service import student_service
from dispatch_sys.services.student_update_service import student_update_service
from events.signals import student_registration_requested, student_update_requested, student_requested, \
    student_all_requested
from services.student_reg_service import register_student


@receiver(student_registration_requested)
def handle_student_registration(sender, data, callback, **kwargs):
    # send the data the student reg function
    result = register_student(sender=sender, data=data, callback=callback)
    callback(result)


@receiver(student_update_requested)
def handle_student_update(sender, data, callback, pk, **kwargs):
    # send the data to the student update function
    result = student_update_service(sender=sender, data=data, callback=callback, pk=pk)
    callback(result)


@receiver(student_all_requested)
def handle_all_student(sender, data, callback, **kwargs):
    # send the data to the student update function
    result = student_all_service(sender=sender, data=data, callback=callback)
    callback(result)


@receiver(student_requested)
def handle_student(sender, data, callback, pk, **kwargs):
    # send the data to the student update function
    result = student_service(sender=sender, data=data, callback=callback, pk=pk)
    callback(result)
