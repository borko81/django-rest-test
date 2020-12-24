from django.shortcuts import render
from rest_framework import generics

from .serializers import GroupSerialize, SimpleSerialize, RecepiesSerializer
from .models import Grops, Simples, Recepies


class GroupListView(generics.ListCreateAPIView):
    serializer_class = GroupSerialize
    queryset = Grops.objects.all()


class SimpleListView(generics.ListCreateAPIView):
    serializer_class = SimpleSerialize
    queryset = Simples.objects.all()


class RecepiListView(generics.ListCreateAPIView):
    serializer_class = RecepiesSerializer
    queryset = Recepies.objects.all()
