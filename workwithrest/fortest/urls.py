from django.urls import path
from . import views

urlpatterns = [
    path('case_one/', views.brutal_funtion, name='brutal_function'),
]