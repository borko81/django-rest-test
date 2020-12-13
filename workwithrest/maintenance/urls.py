from django.urls import path
from .views import type_list, type_details

urlpatterns = [
    path('', type_list, name='type_list'),
    path('<int:pk>/', type_details, name='type_details'),
]