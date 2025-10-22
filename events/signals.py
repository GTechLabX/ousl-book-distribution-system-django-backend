from django.dispatch import Signal

# API publishes this signal for student creation
user_login_requested = Signal()
user_register_requested = Signal()
student_registration_requested = Signal()
user_password_reset_requested = Signal()
