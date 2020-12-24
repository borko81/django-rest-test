from rest_framework import serializers
from .models import Grops, Simples, Recepies


class GroupSerialize(serializers.ModelSerializer):
    class Meta:
        model = Grops
        fields = 'id name razpad'.split()


class SimpleSerialize(serializers.ModelSerializer):
    group_display = serializers.CharField(source='group.name')

    class Meta:
        model = Simples
        fields = 'id name quantity group group_display'.split()


class RecepiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepies
        fields = '__all__'
