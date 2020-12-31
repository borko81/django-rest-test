from django.shortcuts import render
from rest_framework import generics
from .serializers import BasicSerializer, FullSerializer
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User


class EmployeeViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasicSerializer
        elif self.request.method == 'POST':
            return FullSerializer
