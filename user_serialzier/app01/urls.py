from django.urls import path, include
from .views import EmployeeViewSet


urlpatterns = [
    path('emp/', EmployeeViewSet.as_view())
]
