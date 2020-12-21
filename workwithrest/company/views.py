from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

# from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.viewsets import GenericViewSet

from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

from .models import Company, OwnerCompany
from .serializers import Basic, Full, OnwerCompanySerializer


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permision(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.owner == obj.owner


class CompanyViewSet(ListCreateAPIView):
    '''
        List companys, small info in get
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
    # permission_classes = [IsAuthorOrReadOnly]
    serializer_class = OnwerCompanySerializer
    queryset = OwnerCompany.objects.all()


def show_me_all(request):
    template_name = 'index.html'
    return render(request, template_name)