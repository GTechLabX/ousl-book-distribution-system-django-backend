from django.dispatch import receiver

from dispatch_sys.services.acc_creation_services import create_staff_service
from dispatch_sys.services.book_issue_services import book_issue_service
from dispatch_sys.services.book_reservation_services import make_book_reservation_service
from dispatch_sys.services.book_services import book_delete_service, book_update_service, book_show_service, \
    book_all_service, book_add_service
from dispatch_sys.services.center_book_services import center_book_add_service, center_book_all_service, \
    center_book_show_service, center_book_update_service, center_book_delete_service
from dispatch_sys.services.center_services import center_delete_service, center_update_service, center_show_service, \
    center_add_service, center_all_service
from dispatch_sys.services.course_services import course_add_service, course_all_service, course_show_service, \
    course_update_service, course_delete_service
from dispatch_sys.services.dashboard_service import dashboard_service
from dispatch_sys.services.degree_program_course_services import degree_program_course_delete_service, \
    degree_program_course_update_service, degree_program_course_show_service, degree_program_course_all_service, \
    degree_program_course_add_service
from dispatch_sys.services.degree_program_service import degree_program_add_service, degree_program_delete_service, \
    degree_program_update_service, degree_program_show_service, degree_program_all_service
from dispatch_sys.services.department_service import *
from dispatch_sys.services.district_services import district_all_service, district_show_service, \
    district_delete_service, district_update_service, district_add_service
from dispatch_sys.services.faculty_service import *
from dispatch_sys.services.qr_services import get_student_from_qr_service
from dispatch_sys.services.received_book_services import received_book_delete_service, received_book_update_service, \
    received_book_show_service, received_book_all_service, received_book_add_service
from dispatch_sys.services.student_course_services import student_course_delete_service, student_course_update_service, \
    student_course_show_service, student_course_all_service, student_course_add_service
from dispatch_sys.services.student_service import *
from dispatch_sys.services.test_service import test_service
from events.signals.book_reservation_signals import make_book_reservation_requested
from events.signals.book_signals import book_delete_requested, book_update_requested, book_show_requested, \
    book_all_show_requested, book_add_requested
from events.signals.center_book_signals import center_book_add_requested, center_book_all_show_requested, \
    center_book_show_requested, center_book_update_requested, center_book_delete_requested
from events.signals.center_signals import center_delete_requested, center_update_requested, center_show_requested, \
    center_add_requested, center_all_show_requested
from events.signals.course_signals import course_add_requested, course_all_show_requested, course_show_requested, \
    course_update_requested, course_delete_requested
from events.signals.custom_function_signals import book_issue_requested
from events.signals.degree_program_course_signals import degree_program_course_delete_requested, \
    degree_program_course_update_requested, degree_program_course_show_requested, \
    degree_program_course_all_show_requested, degree_program_course_add_requested
from events.signals.degree_program_signals import degree_program_add_requested, degree_program_delete_requested, \
    degree_program_update_requested, degree_program_show_requested, degree_program_all_show_requested
from events.signals.district_signals import district_all_show_requested, district_show_requested, \
    district_delete_requested, district_update_requested, district_add_requested
from events.signals.received_book_signals import received_book_delete_requested, received_book_update_requested, \
    received_book_show_requested, received_book_all_show_requested, received_book_add_requested
from events.signals.signals import student_registration_requested, student_update_requested, \
    student_all_requested, student_requested, student_delete_requested, testAPI, create_staff_requested, \
    dashboard_show_requested
from events.signals.faculty_signals import *
from events.signals.department_signals import *
from events.signals.student_course_signals import student_course_delete_requested, student_course_update_requested, \
    student_course_show_requested, student_course_all_show_requested, student_course_add_requested


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
    # send the data to the faculty add function
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
def handle_department_show(sender, callback, **kwargs):
    result = department_show_service(sender=sender, callback=callback, **kwargs)
    callback(result)


@receiver(department_update_requested)
def handle_department_update(sender, callback, pk, **kwargs):
    result = department_update_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


@receiver(department_delete_requested)
def handle_department_delete(sender, callback, pk, **kwargs):
    result = department_delete_service(sender=sender, callback=callback, pk=pk, **kwargs)
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>

@receiver(degree_program_add_requested)
def handle_degree_program_add(sender, data, callback, **kwargs):
    result = degree_program_add_service(
        sender=sender,
        data=data,
        callback=callback,
        **kwargs
    )
    callback(result)


@receiver(degree_program_all_show_requested)
def handle_degree_program_all_show(sender, callback, **kwargs):
    result = degree_program_all_service(
        sender=sender,
        callback=callback,
        **kwargs
    )
    callback(result)


@receiver(degree_program_show_requested)
def handle_degree_program_show(sender, callback, pk, **kwargs):
    result = degree_program_show_service(
        sender=sender,
        callback=callback,
        pk=pk,
        **kwargs
    )
    callback(result)


@receiver(degree_program_update_requested)
def handle_degree_program_update(sender, callback, pk, data=None, **kwargs):
    result = degree_program_update_service(
        sender=sender,
        data=data,
        callback=callback,
        pk=pk,
        **kwargs
    )
    callback(result)


@receiver(degree_program_delete_requested)
def handle_degree_program_delete(sender, callback, pk, **kwargs):
    result = degree_program_delete_service(
        sender=sender,
        callback=callback,
        pk=pk,
        **kwargs
    )
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>

@receiver(course_add_requested)
def handle_course_add(sender, data, callback, **kwargs):
    result = course_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(course_all_show_requested)
def handle_course_all(sender, callback, **kwargs):
    result = course_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(course_show_requested)
def handle_course_show(sender, callback, pk, **kwargs):
    result = course_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(course_update_requested)
def handle_course_update(sender, data, callback, pk, **kwargs):
    result = course_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(course_delete_requested)
def handle_course_delete(sender, callback, pk, **kwargs):
    result = course_delete_service(sender, callback, pk, **kwargs)
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>

@receiver(book_add_requested)
def handle_book_add(sender, data, callback, **kwargs):
    result = book_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(book_all_show_requested)
def handle_book_all(sender, callback, **kwargs):
    result = book_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(book_show_requested)
def handle_book_show(sender, callback, pk, **kwargs):
    result = book_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(book_update_requested)
def handle_book_update(sender, data, callback, pk, **kwargs):
    result = book_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(book_delete_requested)
def handle_book_delete(sender, callback, pk, **kwargs):
    result = book_delete_service(sender, callback, pk, **kwargs)
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>

@receiver(center_add_requested)
def handle_center_add(sender, data, callback, **kwargs):
    result = center_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(center_all_show_requested)
def handle_center_all(sender, callback, **kwargs):
    result = center_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(center_show_requested)
def handle_center_show(sender, callback, pk, **kwargs):
    result = center_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(center_update_requested)
def handle_center_update(sender, data, callback, pk, **kwargs):
    result = center_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(center_delete_requested)
def handle_center_delete(sender, callback, pk, **kwargs):
    result = center_delete_service(sender, callback, pk, **kwargs)
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>

receiver(student_course_add_requested)


def handle_student_course_add(sender, data, callback, **kwargs):
    result = student_course_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(student_course_all_show_requested)
def handle_student_course_all(sender, callback, **kwargs):
    result = student_course_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(student_course_show_requested)
def handle_student_course_show(sender, callback, pk, **kwargs):
    result = student_course_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(student_course_update_requested)
def handle_student_course_update(sender, data, callback, pk, **kwargs):
    result = student_course_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(student_course_delete_requested)
def handle_student_course_delete(sender, callback, pk, **kwargs):
    result = student_course_delete_service(sender, callback, pk, **kwargs)
    callback(result)


# -------------------------------------------------------->>>>>>>>>>>>>>>

@receiver(degree_program_course_add_requested)
def handle_degree_program_course_add(sender, data, callback, **kwargs):
    result = degree_program_course_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(degree_program_course_all_show_requested)
def handle_degree_program_course_all(sender, callback, **kwargs):
    result = degree_program_course_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(degree_program_course_show_requested)
def handle_degree_program_course_show(sender, callback, pk, **kwargs):
    result = degree_program_course_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(degree_program_course_update_requested)
def handle_degree_program_course_update(sender, data, callback, pk, **kwargs):
    result = degree_program_course_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(degree_program_course_delete_requested)
def handle_degree_program_course_delete(sender, callback, pk, **kwargs):
    result = degree_program_course_delete_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(center_book_add_requested)
def handle_center_book_add(sender, data, callback, **kwargs):
    result = center_book_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(center_book_all_show_requested)
def handle_center_book_all(sender, callback, **kwargs):
    result = center_book_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(center_book_show_requested)
def handle_center_book_show(sender, callback, pk, **kwargs):
    result = center_book_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(center_book_update_requested)
def handle_center_book_update(sender, data, callback, pk, **kwargs):
    result = center_book_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(center_book_delete_requested)
def handle_center_book_delete(sender, callback, pk, **kwargs):
    result = center_book_delete_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(received_book_add_requested)
def handle_received_book_add(sender, data, callback, **kwargs):
    result = received_book_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(received_book_all_show_requested)
def handle_received_book_all(sender, callback, **kwargs):
    result = received_book_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(received_book_show_requested)
def handle_received_book_show(sender, callback, pk, **kwargs):
    result = received_book_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(received_book_update_requested)
def handle_received_book_update(sender, data, callback, pk, **kwargs):
    result = received_book_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(received_book_delete_requested)
def handle_received_book_delete(sender, callback, pk, **kwargs):
    result = received_book_delete_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(district_add_requested)
def handle_district_add(sender, data, callback, **kwargs):
    callback(district_add_service(sender, data, callback, **kwargs))


@receiver(district_update_requested)
def handle_district_update(sender, data, callback, pk, **kwargs):
    callback(district_update_service(sender, data, pk, callback, **kwargs))


@receiver(district_delete_requested)
def handle_district_delete(sender, callback, pk, **kwargs):
    callback(district_delete_service(sender, pk, callback, **kwargs))


@receiver(district_show_requested)
def handle_district_show(sender, callback, pk, **kwargs):
    callback(district_show_service(sender, pk, callback, **kwargs))


@receiver(district_all_show_requested)
def handle_district_all(sender, callback, **kwargs):
    callback(district_all_service(sender, callback, **kwargs))


@receiver(book_issue_requested)
def handle_book_issue(sender, data, callback, **kwargs):
    result = book_issue_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(create_staff_requested)
def handle_create_staff(sender, data, callback, **kwargs):
    result = create_staff_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(testAPI)
def testAPI_get(sender, callback, **kwargs):
    # send the data the student reg function
    result = register_student(sender=sender, callback=callback, **kwargs)
    callback(result)


@receiver(make_book_reservation_requested)
def handle_make_book_reservation(sender, data, callback, uuid, **kwargs):
    callback(make_book_reservation_service(sender, data, uuid, **kwargs))


@receiver(dashboard_show_requested)
def handle_dashboard_show(sender, callback, **kwargs):
    callback(dashboard_service(sender, callback,  **kwargs))
