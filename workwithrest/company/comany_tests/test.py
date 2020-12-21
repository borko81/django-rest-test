from company.models import Company
from django.test import TestCase


class MyTestClass(TestCase):
    def setUp(self):
        Company.objects.create(name='UnrealSoft', description='Some Desc', website='https://somewebsite.com', city='Velingrad')

    def test_count_of_company(self):
        self.assertEqual(Company.objects.all().count(), 1)

    def test_first_param(self):
        '''Testing name for first param'''
        name = Company.objects.get(id=1)
        self.assertEqual(name.name, 'UnrealSoft')
