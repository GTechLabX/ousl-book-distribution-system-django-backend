from django.dispatch import Signal

# API publishes this signal for student creation
user_login_requested = Signal()
user_register_requested = Signal()
user_password_reset_requested = Signal()
user_password_reset_confirm_requested = Signal()


student_registration_requested = Signal()
student_update_requested = Signal()
student_all_requested = Signal()
student_requested = Signal()
