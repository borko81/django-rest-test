from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet

router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')

urlpatterns = [
    re_path('^', include(router.urls))
]