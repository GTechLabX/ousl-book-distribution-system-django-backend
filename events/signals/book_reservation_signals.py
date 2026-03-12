from django.dispatch import Signal

book_reservation_add_requested = Signal()
book_reservation_update_requested = Signal()
book_reservation_delete_requested = Signal()
book_reservation_show_requested = Signal()
book_reservation_all_show_requested = Signal()



#student side

make_book_reservation_requested = Signal()
