from django.apps import AppConfig


class DispatchSysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dispatch_sys'

    def ready(self):
        from events.signals.signals import student_registration_requested, student_update_requested, student_requested, \
            student_all_requested, student_delete_requested
        from .services.student_service import student_all_service, student_delete_service, student_update_service, \
            student_service, register_student

        from events.signals.faculty_signals import faculty_show_requested, faculty_add_requested, \
            faculty_update_requested, faculty_delete_requested, faculty_all_show_requested
        from .services.faculty_service import faculty_update_service, faculty_show_service, faculty_delete_service, \
            faculty_add_service, faculty_all_service

        from events.signals.department_signals import department_delete_requested, department_show_requested, \
            department_all_show_requested, department_update_requested, department_add_requested
        from .services.department_service import department_add_service, department_all_service, \
            department_show_service, department_update_service, department_delete_service

        from dispatch_sys.services.degree_program_service import degree_program_update_service, \
            degree_program_show_service, \
            degree_program_add_service, degree_program_delete_service, degree_program_all_service
        from events.signals.degree_program_signals import degree_program_update_requested, \
            degree_program_show_requested, \
            degree_program_add_requested, degree_program_delete_requested, degree_program_all_show_requested

        from dispatch_sys.services.course_services import course_update_service, course_show_service, \
            course_add_service, \
            course_delete_service, course_all_service
        from events.signals.course_signals import course_update_requested, course_show_requested, course_add_requested, \
            course_delete_requested, course_all_show_requested

        from dispatch_sys.services.book_services import book_update_service, book_show_service, book_delete_service, \
            book_add_service, book_all_service
        from events.signals.book_signals import book_update_requested, book_add_requested, book_show_requested, \
            book_delete_requested, book_all_show_requested

        from dispatch_sys.services.center_services import center_update_service, center_show_service, \
            center_add_service, \
            center_delete_service, center_all_service
        from events.signals.center_signals import center_update_requested, center_add_requested, \
            center_delete_requested, \
            center_all_show_requested, center_show_requested


        student_registration_requested.connect(register_student)
        student_requested.connect(student_service)
        student_update_requested.connect(student_update_service)
        student_delete_requested.connect(student_delete_service)
        student_all_requested.connect(student_all_service)

        faculty_add_requested.connect(faculty_add_service)
        faculty_update_requested.connect(faculty_update_service)
        faculty_delete_requested.connect(faculty_delete_service)
        faculty_show_requested.connect(faculty_show_service)
        faculty_all_show_requested.connect(faculty_all_service)

        department_update_requested.connect(department_update_service)
        department_show_requested.connect(department_show_service)
        department_add_requested.connect(department_add_service)
        department_delete_requested.connect(department_delete_service)
        department_all_show_requested.connect(department_all_service)

        degree_program_update_requested.connect(degree_program_update_service)
        degree_program_show_requested.connect(degree_program_show_service)
        degree_program_add_requested.connect(degree_program_add_service)
        degree_program_delete_requested.connect(degree_program_delete_service)
        degree_program_all_show_requested.connect(degree_program_all_service)

        course_update_requested.connect(course_update_service)
        course_show_requested.connect(course_show_service)
        course_add_requested.connect(course_add_service)
        course_delete_requested.connect(course_delete_service)
        course_all_show_requested.connect(course_all_service)

        book_update_requested.connect(book_update_service)
        book_show_requested.connect(book_show_service)
        book_add_requested.connect(book_add_service)
        book_delete_requested.connect(book_delete_service)
        book_all_show_requested.connect(book_all_service)

        center_update_requested.connect(center_update_service)
        center_show_requested.connect(center_show_service)
        center_add_requested.connect(center_add_service)
        center_delete_requested.connect(center_delete_service)
        center_all_show_requested.connect(center_all_service)
