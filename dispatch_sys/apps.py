from django.apps import AppConfig


class DispatchSysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dispatch_sys'

    def ready(self):
        from events.signals.signals import student_registration_requested, student_update_requested,student_requested,student_all_requested,student_delete_requested
        from .services.student_reg_service import register_student
        from .services.student_service import student_service
        from .services.student_all_service import student_all_service
        from .services.student_update_service import student_update_service
        from .services.student_delete_service import student_delete_service

        student_registration_requested.connect(register_student)
        student_requested.connect(student_service)
        student_update_requested.connect(student_update_service)
        student_delete_requested.connect(student_delete_service)
        student_all_requested.connect(student_all_service)
