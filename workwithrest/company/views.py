from rest_framework import viewsets

from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Company, OwnerCompany
from .serializers import CompanySerialzier, OnwerCompanySerializer


class CompanyViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = CompanySerialzier
    queryset = Company.objects.all()


class OwnerCompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OnwerCompanySerializer
    queryset = OwnerCompany.objects.all()
