from django.dispatch import Signal

# API publishes this signal for student creation

student_registration_requested = Signal()
user_login_requested = Signal()
user_register_requested = Signal()