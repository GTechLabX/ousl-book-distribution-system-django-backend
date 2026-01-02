from django.db.models.signals import post_migrate
from django.dispatch import receiver
from dispatch_sys.models import District

DISTRICTS = [
    "Ampara", "Anuradhapura", "Badulla", "Batticaloa", "Colombo",
    "Galle", "Gampaha", "Hambantota", "Jaffna", "Kalutara", "Kandy",
    "Kegalle", "Kilinochchi", "Kurunegala", "Mannar", "Matale",
    "Matara", "Monaragala", "Mullaitivu", "Nuwara Eliya", "Polonnaruwa",
    "Puttalam", "Ratnapura", "Trincomalee", "Vavuniya"
]


@receiver(post_migrate)
def seed_sri_lankan_districts(sender, **kwargs):
    if sender.name == 'dispatch_sys':
        for name in DISTRICTS:
            District.objects.get_or_create(district_name=name)
