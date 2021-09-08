from rest_framework import serializers

from .models import Groups, Simple


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class SimpleOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Simple
        fields = '__all__'


class GroupAllSerializer(serializers.ModelSerializer):
    simples = SimpleOnlySerializer(many=True, required=False)

    class Meta:
        model = Groups
        fields = '__all__'
