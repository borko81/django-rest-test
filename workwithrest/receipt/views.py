from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer, RestaurantSerializer, IngredientSerializer
from .models import Recipe, Restaurant, Ingredient
from django.http import Http404
from rest_framework import status


class Restaurants(APIView):

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializers = RecipeSerializer(restaurants, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):
    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except ObjectDoesNotExist:
            raise Http404
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)