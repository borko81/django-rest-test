from rest_framework import generics

from .serializers import GroupSerialize, SimpleSerialize, RecepiesSerializer, RecepiesIngrediencSerializer
from .models import Grops, Simples, Recepies, RecipeIngredient


class GroupListView(generics.ListCreateAPIView):
    serializer_class = GroupSerialize
    queryset = Grops.objects.all()


class SimpleListView(generics.ListCreateAPIView):
    serializer_class = SimpleSerialize
    queryset = Simples.objects.all()


class RecepiListView(generics.ListCreateAPIView):
    serializer_class = RecepiesSerializer
    queryset = Recepies.objects.all()


class RecepiDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecepiesSerializer
    queryset = Recepies.objects.all()


class RecepiIng(generics.ListCreateAPIView):
    serializer_class = RecepiesIngrediencSerializer
    queryset = RecipeIngredient.objects.all()


class RecepiIngDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecepiesIngrediencSerializer
    queryset = RecipeIngredient.objects.all()