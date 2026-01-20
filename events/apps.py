from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self):
        import events.signals.district_signal
        import events.signals.signals
        import events.signals.student_qr_signals
        import events.signals.custom_function_signals
