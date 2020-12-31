from rest_framework import serializers
from django.contrib.auth.models import User


def factory_serializer_employee(type='basic'):

    if type == 'basic':
        my_field = 'username email'.split()
    elif type == 'full':
        my_field = 'username email password'.split()

    class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
            fields = my_field
            model = User
            password = serializers.CharField(required=True)

    return EmployeeSerializer


BasicSerializer = factory_serializer_employee('basic')
FullSerializer = factory_serializer_employee('full')
