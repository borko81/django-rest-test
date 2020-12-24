from rest_framework import serializers
from .models import Grops, Simples, RecipeIngredient, Recepies


class GroupSerialize(serializers.ModelSerializer):
    class Meta:
        model = Grops
        fields = '__all__'


class SimpleSerialize(serializers.ModelSerializer):
    group_display = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = Simples
        fields = 'pk name quantity group group_display'.split()


class RecepiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recepies
        fields = '__all__'


class RecepiesIngrediencSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredient
        fields = '__all__'
