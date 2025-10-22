from django.apps import AppConfig


class AuthsysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_sys'

    def ready(self):
        from events.signals import user_login_requested, user_register_requested
        from .services.login_service import login_service
        from .services.register_service import register_service

        user_login_requested.connect(login_service)
        user_register_requested.connect(register_service)

