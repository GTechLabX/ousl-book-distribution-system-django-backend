from django.dispatch import receiver

from auth_sys.services.logout_service import user_logout_service
from auth_sys.services.password_reset_confirm_service import user_password_reset_confirm_service
from auth_sys.services.password_reset_service import user_password_reset_service
from auth_sys.services.register_service import register_service
from auth_sys.services.user_services import user_add_service, user_update_service, user_delete_service, \
    user_show_service, user_all_service
from events.signals.auth_signals.user_signals import user_add_requested, user_update_requested, user_delete_requested, \
    user_show_requested, user_all_show_requested
from events.signals.signals import user_login_requested, user_register_requested, user_password_reset_requested, \
    user_password_reset_confirm_requested, user_logout_requested
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


@receiver(user_password_reset_confirm_requested)
def handle_user_password_reset_confirm(sender, data, callback, **kwargs):
    # send the data to the password reset confirm
    result = user_password_reset_confirm_service(sender=sender, data=data, callback=callback, **kwargs)
    callback(result)


@receiver(user_add_requested)
def handle_user_add(sender, data, callback, **kwargs):
    result = user_add_service(sender, data, callback, **kwargs)
    callback(result)


@receiver(user_update_requested)
def handle_user_update(sender, data, callback, pk, **kwargs):
    result = user_update_service(sender, data, callback, pk, **kwargs)
    callback(result)


@receiver(user_delete_requested)
def handle_user_delete(sender, callback, pk, **kwargs):
    result = user_delete_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(user_show_requested)
def handle_user_show(sender, callback, pk, **kwargs):
    result = user_show_service(sender, callback, pk, **kwargs)
    callback(result)


@receiver(user_all_show_requested)
def handle_user_all(sender, callback, **kwargs):
    result = user_all_service(sender, callback, **kwargs)
    callback(result)


@receiver(user_logout_requested)
def handle_user_logout(sender, callback, user=None, refresh_token=None, **kwargs):
    """
    Listener for logout signal
    """
    result = user_logout_service(
        sender=sender,
        callback=callback,
        user=user,
        refresh_token=refresh_token,
        **kwargs
    )
    callback(result)
