from django.urls import path

from app_one.views import index, return_city_population, profile

urlpatterns = [
    path('', index, name='index'),
    path('total/', return_city_population, name='population'),
    path('profile/', profile, name='profile'),
]