from django.apps import AppConfig


class DispatchSysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dispatch_sys'

    def ready(self):
        from events.signals import student_registration_requested
        from .services.student_service import register_student

        student_registration_requested.connect(register_student)
