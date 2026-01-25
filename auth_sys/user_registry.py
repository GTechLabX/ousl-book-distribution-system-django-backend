from events.signals.auth_signals.user_signals import (
    user_add_requested,
    user_update_requested,
    user_delete_requested,
    user_show_requested,
    user_all_show_requested,
)

from auth_sys.services.user_services import (
    user_add_service,
    user_update_service,
    user_delete_service,
    user_show_service,
    user_all_service,
)

user_add_requested.connect(
    user_add_service,
    dispatch_uid="user_add_service"
)

user_update_requested.connect(
    user_update_service,
    dispatch_uid="user_update_service"
)

user_delete_requested.connect(
    user_delete_service,
    dispatch_uid="user_delete_service"
)

user_show_requested.connect(
    user_show_service,
    dispatch_uid="user_show_service"
)

user_all_show_requested.connect(
    user_all_service,
    dispatch_uid="user_all_service"
)
