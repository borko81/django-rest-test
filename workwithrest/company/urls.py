from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, OwnerCompanyViewSet, CompanyViewDetail, show_me_all

router = DefaultRouter()
router.register('owner', OwnerCompanyViewSet, basename='owner-company')

urlpatterns = [
    # re_path('^', include(router.urls)),
    path('', CompanyViewSet.as_view(), name='company'),
    path('<int:pk>/', CompanyViewDetail.as_view(), name='owner-company'),
    path('showall/', show_me_all, name='show_me_all'),
]

urlpatterns += router.urls
