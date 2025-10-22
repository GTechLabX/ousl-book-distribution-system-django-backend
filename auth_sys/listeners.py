from django.dispatch import receiver
from events.signals import user_login_requested
from services.login_service import login_service


@receiver(user_login_requested)
def handle_user_login(sender, data, callback, **kwargs):
    # send the data the student login function
    result = login_service(data)
    callback(result)
