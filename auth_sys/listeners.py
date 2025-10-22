from django.dispatch import receiver

from auth_sys.services.register_service import register_service
from events.signals import user_login_requested, user_register_requested, user_password_reset_requested
from services.login_service import login_service


@receiver(user_login_requested)
def handle_user_login(sender, data, callback, **kwargs):
    # send the data the student login function
    result = login_service(sender=sender, data=data, callback=callback)
    callback(result)


@receiver(user_register_requested)
def handle_user_register(sender, data, callback, **kwargs):
    # send the data the student register function
    result = register_service(sender=sender, data=data, callback=callback)
    callback(result)


@receiver(user_password_reset_requested)
def handle_user_password_reset(sender, data, callback, **kwargs):
    # send the data to the user password reset
    result = user_password_reset_service(sender=sender, data=data, callback=callback, **kwargs)
    callback(result)
