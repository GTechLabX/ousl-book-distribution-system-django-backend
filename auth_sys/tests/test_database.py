from django.test import TestCase
from auth_sys.models import Country


class CountryModelTest(TestCase):
    def test_country_creation(self):
        country = Country.objects.create(country_name="Sri lanka", country_code="LK", country_tel_code="+94")
        self.assertEqual(country.country_name, "Sri lanka")
        self.assertEqual(country.country_code, "LK")
        self.assertEqual(country.country_tel_code, "+94")
        self.assertEqual(str(country), "country name: Sri lanka")
