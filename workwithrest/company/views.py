from rest_framework import viewsets

from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Company, OwnerCompany
from .serializers import Basic, Full, OnwerCompanySerializer


class CompanyViewSet(ListCreateAPIView):
    '''
        List companys, small info in get, 
        detailed shows in post
    '''
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return Basic
        return Full


class CompanyViewDetail(RetrieveUpdateDestroyAPIView):
    '''
        Detail view of company, full set of fields.
    '''
    queryset = Company.objects.all()
    serializer_class = Full


class OwnerCompanyViewSet(viewsets.ModelViewSet):
    '''
        This is owner view
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OnwerCompanySerializer
    queryset = OwnerCompany.objects.all()
