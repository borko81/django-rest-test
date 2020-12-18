from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, OwnerCompanyViewSet

router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
router.register('owner', OwnerCompanyViewSet, basename='owner-company')

urlpatterns = [
    re_path('^', include(router.urls))
]
