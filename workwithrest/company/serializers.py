from rest_framework import serializers

from .models import Company, OwnerCompany


class CompanySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class OnwerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerCompany
        fields = '__all__'
