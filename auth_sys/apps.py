from django.apps import AppConfig


class AuthsysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_sys'

    def ready(self):
        from events.signals import user_login_requested, user_register_requested, user_password_reset_requested, user_password_reset_confirm_requested
        from .services.login_service import login_service
        from .services.register_service import register_service
        from .services.password_reset_service import user_password_reset_service
        from .services.password_reset_confirm_service import user_password_reset_confirm_service

        user_login_requested.connect(login_service)
        user_register_requested.connect(register_service)
        user_password_reset_requested.connect(user_password_reset_service)
        user_password_reset_confirm_requested.connect(user_password_reset_confirm_service)

