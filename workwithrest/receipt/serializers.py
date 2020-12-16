from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Recipe, Restaurant, Ingredient
import base64
from django.conf import settings
import os


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = 'id name'.split()


class RecipeSerializer(serializers.ModelSerializer):
    #thumbnail = serializers.SerializerMethodField('encode_thumbnail')
    ingredients = serializers.SerializerMethodField('get_ingredients')

    # def encode_thumbnail(self, recipe):
    #     with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), 'rb') as image:
    #         return base64.b64encode(image.read())

    def get_ingredients(self, recipe):
        try:
            recipe_ingredients = Ingredient.objects.filter(recipe__id=recipe.id)
            return IngredientSerializer(recipe_ingredients, many=True).data
        except ObjectDoesNotExist:
            return None

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients")
        restaurant = Restaurant.objects.create(**validated_data)
        validated_data["restaurant"] = restaurant
        recipe = Recipe.objects.create(**validated_data)

        if ingredients_data:
            for ingredient_dict in ingredients_data:
                ingredient = Ingredient(name=ingredient_dict['name'])
                ingredient.save()
                ingredient.recipe.add(recipe)
        return recipe

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'type', 'thumbnail', 'ingredients']

