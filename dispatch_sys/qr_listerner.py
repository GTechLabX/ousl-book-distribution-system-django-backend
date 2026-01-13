from django.dispatch import receiver

from dispatch_sys.services.qr_services import get_student_from_qr_service
from events.signals.qr_signals import student_qr_scan_requested


@receiver(student_qr_scan_requested)
def handle_student_qr_scan(sender, callback, qr_image, **kwargs):
    """
    Signal handler for student QR scan.
    Delegates logic to dispatch service, then calls callback with result.
    """
    # No need for sender here
    result = get_student_from_qr_service(qr_image_file=qr_image)
    # call the callback to update the response
    callback(result)
