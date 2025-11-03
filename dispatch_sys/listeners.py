from django.dispatch import receiver

from dispatch_sys.services.faculty_add_service import faculty_add_service
from dispatch_sys.services.faculty_all_service import faculty_all_service
from dispatch_sys.services.faculty_delete_service import faculty_delete_service
from dispatch_sys.services.faculty_show_service import faculty_show_service
from dispatch_sys.services.faculty_update_service import faculty_update_service
from dispatch_sys.services.student_all_service import student_all_service
from dispatch_sys.services.student_delete_service import student_delete_service
from dispatch_sys.services.student_service import student_service
from dispatch_sys.services.student_update_service import student_update_service
from events.signals import student_registration_requested, student_update_requested, student_requested, \
    student_all_requested, student_delete_requested, faculty_add_requested, faculty_all_show_requested, \
    faculty_show_requested, faculty_update_requested, faculty_delete_requested, department_add_requested, \
    department_all_show_requested, department_show_requested, department_update_requested, department_delete_requested
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
def handle_all_student(sender, callback, **kwargs):
    # send the data to the student update function
    result = student_all_service(sender=sender, callback=callback, **kwargs)
    callback(result)


@receiver(student_requested)
def handle_student(sender, data, callback, pk, **kwargs):
    # send the data to the student update function
    result = student_service(sender=sender, data=data, callback=callback, pk=pk, **kwargs)
    callback(result)


@receiver(student_delete_requested)
def handle_student_delete(sender, callback, pk, **kwargs):
    # send the data to the student update function
    result = student_delete_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>

@receiver(faculty_add_requested)
def handle_faculty_add(sender, data, callback, **kwargs):
    # send the data to the student update function
    result = faculty_add_service(sender=sender, data=data, callback=callback, **kwargs)
    callback(result)


@receiver(faculty_all_show_requested)
def handle_faculty_all_show(sender, callback, **kwargs):
    # send the data to the student update function
    result = faculty_all_service(sender=sender, callback=callback, **kwargs)
    callback(result)


@receiver(faculty_show_requested)
def handle_faculty_show(sender, callback, pk, **kwargs):
    # send the data to the student update function
    result = faculty_show_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


@receiver(faculty_update_requested)
def handle_faculty_update(sender, callback, pk, **kwargs):
    # send the data to the student update function
    result = faculty_update_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


@receiver(faculty_delete_requested)
def handle_faculty_delete(sender, callback, pk, **kwargs):
    # send the data to the student update function
    result = faculty_delete_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>


@receiver(department_add_requested)
def handle_department_add(sender, data, callback, **kwargs):
    result = department_add_service(sender=sender, data=data, callback=callback, **kwargs)
    callback(result)


@receiver(department_all_show_requested)
def handle_department_all_show(sender, callback, **kwargs):
    result = department_all_service(sender=sender, callback=callback, **kwargs)
    callback(result)


@receiver(department_show_requested)
def handle_department_show(sender, callback, pk, **kwargs):
    result = department_show_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


@receiver(department_update_requested)
def handle_department_update(sender, callback, pk, **kwargs):
    result = department_update_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


@receiver(department_delete_requested)
def handle_department_delete(sender, callback, pk, **kwargs):
    result = department_delete_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)
