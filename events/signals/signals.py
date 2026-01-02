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
student_delete_requested = Signal()


faculty_add_requested = Signal()
faculty_all_show_requested = Signal()
faculty_show_requested = Signal()
faculty_update_requested = Signal()
faculty_delete_requested = Signal()


department_add_requested = Signal()
department_all_show_requested = Signal()
department_show_requested = Signal()
department_update_requested = Signal()
department_delete_requested = Signal()
