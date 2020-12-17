from django.shortcuts import render

from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.viewsets import GenericViewSet

from .models import Company
from .serializers import CompanySerialzier


class CompanyViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = CompanySerialzier
    queryset = Company.objects.all()