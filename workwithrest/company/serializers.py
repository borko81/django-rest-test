from rest_framework import serializers

from .models import Company, OwnerCompany


class OnwerCompanySerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = OwnerCompany
        fields = 'pk company company_name owner owner_name'.split()
        lookup_field = 'pk'


def company_Serializer_factory(type='basic'):
    if type == 'basic':
        res_fields = 'pk name'.split()
    elif type == 'full':
        res_fields = 'pk name description website city'.split()

    class CompanySerialzier(serializers.ModelSerializer):
        class Meta:
            fields = res_fields
            model = Company

    return CompanySerialzier


Basic = company_Serializer_factory('basic')
Full = company_Serializer_factory('full')
