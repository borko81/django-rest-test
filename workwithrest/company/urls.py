from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, OwnerCompanyViewSet, CompanyViewDetail

router = DefaultRouter()
router.register('owner', OwnerCompanyViewSet, basename='owner-company')

urlpatterns = [
    # re_path('^', include(router.urls)),
    path('', CompanyViewSet.as_view(), name='company'),
    path('<int:pk>/', CompanyViewDetail.as_view(), name='owner-company'),
]

urlpatterns += router.urls
