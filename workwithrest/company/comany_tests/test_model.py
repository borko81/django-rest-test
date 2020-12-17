from django.test import TestCase

from .factories import CompanyFactory

# Not finish
class CompanyTestCase(TestCase):
    def test_str(self):
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)
