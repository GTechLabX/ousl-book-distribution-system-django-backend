from django.core.management.base import BaseCommand
from auth_sys.models import Country

COUNTRIES = {
    {"name": "sri lanka", "code": "LK"},
}


class Command(BaseCommand):
    help = "Seeds the country table with initial data"

    def handle(self, *args, **options):
        for c in COUNTRIES:
            obj, created = Country.objects.get_or_create(
                code=c["code"], defaults={"name": c["name"]}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Added{c['name']}"))
            else:
                self.stdout.write(f"{c['name']} Already exits")

        self.stdout.write(self.style.SUCCESS("✅ Countries seeding complete."))
