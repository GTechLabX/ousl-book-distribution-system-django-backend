from django.dispatch import Signal

user_add_requested = Signal()
user_update_requested = Signal()
user_delete_requested = Signal()
user_show_requested = Signal()
user_all_show_requested = Signal()
