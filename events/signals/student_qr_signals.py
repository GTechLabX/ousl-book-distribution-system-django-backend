import qrcode
from io import BytesIO
from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver

from dispatch_sys.models import Student, StudentQRCode


def generate_student_qr(instance):
    """
    Generates a QR code for a StudentQRCode instance.
    """
    qr_data = f"Student ID: {instance.student.id}, Name: {instance.student.student_name}, Email: {instance.student.email}"
    qr_img = qrcode.make(qr_data)

    # Save the image to a BytesIO object
    blob = BytesIO()
    qr_img.save(blob, 'PNG')
    instance.qr_image.save(f'student_{instance.student.id}_qr.png', File(blob), save=False)
    blob.close()


@receiver(post_save, sender=Student)
def create_student_qr(sender, instance, created, **kwargs):
    if created:
        # Create a StudentQRCode instance
        qr_instance = StudentQRCode.objects.create(student=instance)
        generate_student_qr(qr_instance)
        qr_instance.save()
