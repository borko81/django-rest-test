from factory import DjangoModelFactory, Faker

from company.models import Company


class CompanyFactory(DjangoModelFactory):

    class Meta:
        model = Company

    name = 'Unreal'
    description = 'Software'
    website = 'https://unrealsoft.net'
    city = 'Velingrad'
