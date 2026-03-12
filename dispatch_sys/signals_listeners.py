# ===================== STUDENT =====================
from events.signals.signals import (
    student_registration_requested,
    student_requested,
    student_update_requested,
    student_delete_requested,
    student_all_requested,
)

from dispatch_sys.services.student_service import (
    register_student,
    student_service,
    student_update_service,
    student_delete_service,
    student_all_service,
)

student_registration_requested.connect(
    register_student,
    dispatch_uid="student_registration_register_student"
)
student_requested.connect(
    student_service,
    dispatch_uid="student_requested_student_service"
)
student_update_requested.connect(
    student_update_service,
    dispatch_uid="student_update_student_update_service"
)
student_delete_requested.connect(
    student_delete_service,
    dispatch_uid="student_delete_student_delete_service"
)
student_all_requested.connect(
    student_all_service,
    dispatch_uid="student_all_student_all_service"
)

# ===================== FACULTY =====================
from events.signals.faculty_signals import (
    faculty_add_requested,
    faculty_update_requested,
    faculty_delete_requested,
    faculty_show_requested,
    faculty_all_show_requested,
)

from dispatch_sys.services.faculty_service import (
    faculty_add_service,
    faculty_update_service,
    faculty_delete_service,
    faculty_show_service,
    faculty_all_service,
)

faculty_add_requested.connect(
    faculty_add_service,
    dispatch_uid="faculty_add_faculty_add_service"
)
faculty_update_requested.connect(
    faculty_update_service,
    dispatch_uid="faculty_update_faculty_update_service"
)
faculty_delete_requested.connect(
    faculty_delete_service,
    dispatch_uid="faculty_delete_faculty_delete_service"
)
faculty_show_requested.connect(
    faculty_show_service,
    dispatch_uid="faculty_show_faculty_show_service"
)
faculty_all_show_requested.connect(
    faculty_all_service,
    dispatch_uid="faculty_all_faculty_all_service"
)

# ===================== DEPARTMENT =====================
from events.signals.department_signals import (
    department_add_requested,
    department_update_requested,
    department_delete_requested,
    department_show_requested,
    department_all_show_requested,
)

from dispatch_sys.services.department_service import (
    department_add_service,
    department_update_service,
    department_delete_service,
    department_show_service,
    department_all_service,
)

department_add_requested.connect(
    department_add_service,
    dispatch_uid="department_add_department_add_service"
)
department_update_requested.connect(
    department_update_service,
    dispatch_uid="department_update_department_update_service"
)
department_delete_requested.connect(
    department_delete_service,
    dispatch_uid="department_delete_department_delete_service"
)
department_show_requested.connect(
    department_show_service,
    dispatch_uid="department_show_department_show_service"
)
department_all_show_requested.connect(
    department_all_service,
    dispatch_uid="department_all_department_all_service"
)

# ===================== DEGREE PROGRAM =====================
from events.signals.degree_program_signals import (
    degree_program_add_requested,
    degree_program_update_requested,
    degree_program_delete_requested,
    degree_program_show_requested,
    degree_program_all_show_requested,
)

from dispatch_sys.services.degree_program_service import (
    degree_program_add_service,
    degree_program_update_service,
    degree_program_delete_service,
    degree_program_show_service,
    degree_program_all_service,
)

degree_program_add_requested.connect(
    degree_program_add_service,
    dispatch_uid="degree_program_add_degree_program_add_service"
)
degree_program_update_requested.connect(
    degree_program_update_service,
    dispatch_uid="degree_program_update_degree_program_update_service"
)
degree_program_delete_requested.connect(
    degree_program_delete_service,
    dispatch_uid="degree_program_delete_degree_program_delete_service"
)
degree_program_show_requested.connect(
    degree_program_show_service,
    dispatch_uid="degree_program_show_degree_program_show_service"
)
degree_program_all_show_requested.connect(
    degree_program_all_service,
    dispatch_uid="degree_program_all_degree_program_all_service"
)

# ===================== COURSE =====================
from events.signals.course_signals import (
    course_add_requested,
    course_update_requested,
    course_delete_requested,
    course_show_requested,
    course_all_show_requested,
)

from dispatch_sys.services.course_services import (
    course_add_service,
    course_update_service,
    course_delete_service,
    course_show_service,
    course_all_service,
)

course_add_requested.connect(
    course_add_service,
    dispatch_uid="course_add_course_add_service"
)
course_update_requested.connect(
    course_update_service,
    dispatch_uid="course_update_course_update_service"
)
course_delete_requested.connect(
    course_delete_service,
    dispatch_uid="course_delete_course_delete_service"
)
course_show_requested.connect(
    course_show_service,
    dispatch_uid="course_show_course_show_service"
)
course_all_show_requested.connect(
    course_all_service,
    dispatch_uid="course_all_course_all_service"
)

# ===================== BOOK =====================
from events.signals.book_signals import (
    book_add_requested,
    book_update_requested,
    book_delete_requested,
    book_show_requested,
    book_all_show_requested,
)

from dispatch_sys.services.book_services import (
    book_add_service,
    book_update_service,
    book_delete_service,
    book_show_service,
    book_all_service,
)

book_add_requested.connect(
    book_add_service,
    dispatch_uid="book_add_book_add_service"
)
book_update_requested.connect(
    book_update_service,
    dispatch_uid="book_update_book_update_service"
)
book_delete_requested.connect(
    book_delete_service,
    dispatch_uid="book_delete_book_delete_service"
)
book_show_requested.connect(
    book_show_service,
    dispatch_uid="book_show_book_show_service"
)
book_all_show_requested.connect(
    book_all_service,
    dispatch_uid="book_all_book_all_service"
)

# ===================== CENTER =====================
from events.signals.center_signals import (
    center_add_requested,
    center_update_requested,
    center_delete_requested,
    center_show_requested,
    center_all_show_requested,
)

from dispatch_sys.services.center_services import (
    center_add_service,
    center_update_service,
    center_delete_service,
    center_show_service,
    center_all_service,
)

center_add_requested.connect(
    center_add_service,
    dispatch_uid="center_add_center_add_service"
)
center_update_requested.connect(
    center_update_service,
    dispatch_uid="center_update_center_update_service"
)
center_delete_requested.connect(
    center_delete_service,
    dispatch_uid="center_delete_center_delete_service"
)
center_show_requested.connect(
    center_show_service,
    dispatch_uid="center_show_center_show_service"
)
center_all_show_requested.connect(
    center_all_service,
    dispatch_uid="center_all_center_all_service"
)

# ===================== STUDENT COURSE =====================
from events.signals.student_course_signals import (
    student_course_add_requested,
    student_course_update_requested,
    student_course_delete_requested,
    student_course_show_requested,
    student_course_all_show_requested,
)

from dispatch_sys.services.student_course_services import (
    student_course_add_service,
    student_course_update_service,
    student_course_delete_service,
    student_course_show_service,
    student_course_all_service,
)

student_course_add_requested.connect(
    student_course_add_service,
    dispatch_uid="student_course_add_student_course_add_service"
)
student_course_update_requested.connect(
    student_course_update_service,
    dispatch_uid="student_course_update_student_course_update_service"
)
student_course_delete_requested.connect(
    student_course_delete_service,
    dispatch_uid="student_course_delete_student_course_delete_service"
)
student_course_show_requested.connect(
    student_course_show_service,
    dispatch_uid="student_course_show_student_course_show_service"
)
student_course_all_show_requested.connect(
    student_course_all_service,
    dispatch_uid="student_course_all_student_course_all_service"
)

# ===================== Center Student =====================

from events.signals.center_book_signals import (
    center_book_add_requested,
    center_book_update_requested,
    center_book_delete_requested,
    center_book_show_requested,
    center_book_all_show_requested,
)

from dispatch_sys.services.center_book_services import (
    center_book_add_service,
    center_book_update_service,
    center_book_delete_service,
    center_book_show_service,
    center_book_all_service,
)

center_book_add_requested.connect(
    center_book_add_service,
    dispatch_uid="center_book_add_center_book_add_service"
)

center_book_update_requested.connect(
    center_book_update_service,
    dispatch_uid="center_book_update_center_book_update_service"
)

center_book_delete_requested.connect(
    center_book_delete_service,
    dispatch_uid="center_book_delete_center_book_delete_service"
)

center_book_show_requested.connect(
    center_book_show_service,
    dispatch_uid="center_book_show_center_book_show_service"
)

center_book_all_show_requested.connect(
    center_book_all_service,
    dispatch_uid="center_book_all_center_book_all_service"
)


# ===================== Received Book =====================

from events.signals.received_book_signals import (
    received_book_add_requested,
    received_book_update_requested,
    received_book_delete_requested,
    received_book_show_requested,
    received_book_all_show_requested,
)

from dispatch_sys.services.received_book_services import (
    received_book_add_service,
    received_book_update_service,
    received_book_delete_service,
    received_book_show_service,
    received_book_all_service,
)

received_book_add_requested.connect(
    received_book_add_service,
    dispatch_uid="received_book_add_received_book_add_service"
)

received_book_update_requested.connect(
    received_book_update_service,
    dispatch_uid="received_book_update_received_book_update_service"
)

received_book_delete_requested.connect(
    received_book_delete_service,
    dispatch_uid="received_book_delete_received_book_delete_service"
)

received_book_show_requested.connect(
    received_book_show_service,
    dispatch_uid="received_book_show_received_book_show_service"
)

received_book_all_show_requested.connect(
    received_book_all_service,
    dispatch_uid="received_book_all_received_book_all_service"
)



from events.signals.book_reservation_signals import (
    book_reservation_add_requested,
    book_reservation_update_requested,
    book_reservation_delete_requested,
    book_reservation_show_requested,
    book_reservation_all_show_requested,
)

from dispatch_sys.services.book_reservation_services import (
    book_reservation_add_service,
    book_reservation_update_service,
    book_reservation_delete_service,
    book_reservation_show_service,
    book_reservation_all_service,
)

book_reservation_add_requested.connect(
    book_reservation_add_service,
    dispatch_uid="book_reservation_add_service"
)

book_reservation_update_requested.connect(
    book_reservation_update_service,
    dispatch_uid="book_reservation_update_service"
)

book_reservation_delete_requested.connect(
    book_reservation_delete_service,
    dispatch_uid="book_reservation_delete_service"
)

book_reservation_show_requested.connect(
    book_reservation_show_service,
    dispatch_uid="book_reservation_show_service"
)

book_reservation_all_show_requested.connect(
    book_reservation_all_service,
    dispatch_uid="book_reservation_all_service"
)



from events.signals.district_signals import (
    district_add_requested,
    district_update_requested,
    district_delete_requested,
    district_show_requested,
    district_all_show_requested,
)

from dispatch_sys.services.district_services import (
    district_add_service,
    district_update_service,
    district_delete_service,
    district_show_service,
    district_all_service,
)

district_add_requested.connect(
    district_add_service,
    dispatch_uid="district_add_service"
)

district_update_requested.connect(
    district_update_service,
    dispatch_uid="district_update_service"
)

district_delete_requested.connect(
    district_delete_service,
    dispatch_uid="district_delete_service"
)

district_show_requested.connect(
    district_show_service,
    dispatch_uid="district_show_service"
)

district_all_show_requested.connect(
    district_all_service,
    dispatch_uid="district_all_service"
)


from events.signals.custom_function_signals import book_issue_requested
from dispatch_sys.services.book_issue_services import book_issue_service

book_issue_requested.connect(
    book_issue_service,
    dispatch_uid="book_issue_service"
)

from events.signals.signals import create_staff_requested
from dispatch_sys.services.acc_creation_services import create_staff_service

create_staff_requested.connect(
    create_staff_service,
    dispatch_uid="create_staff_service"
)


from events.signals.book_reservation_signals import make_book_reservation_requested
from dispatch_sys.services.book_reservation_services import make_book_reservation_service

make_book_reservation_requested.connect(
    make_book_reservation_service,
    dispatch_uid="make_book_reservation"
)

from events.signals.signals import dashboard_show_requested
from dispatch_sys.services.dashboard_service import dashboard_service

dashboard_show_requested.connect(
    dashboard_service,
    dispatch_uid="dashboard_show"
)



from events.signals.signals import center_allocation_view_requested
from dispatch_sys.services.center_book_services import view_center_allocation_service

center_allocation_view_requested.connect(
    view_center_allocation_service,
    dispatch_uid="view_center_allocation_by_center"
)
