from django.test import TestCase

from .factories import CompanyFactory

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workwithrest.settings')
import django
django.setup()


class CompanyTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)