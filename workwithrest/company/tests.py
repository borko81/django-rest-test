from django.test import TestCase

from factory import DjangoModelFactory, Faker

from .models import Company


class CompanyFactor(DjangoModelFactory):
    name = Faker('company')
    description = Faker('text')
    website = Faker('url')
    city = Faker('Velingrad')

    class Meta:
        model = Company


class CompanyTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company = CompanyFactor()
        self.assertEqual(str(company), company.name)