from django.urls import path

from app_one.views import index, return_city_population, profile, show_films, CreateFilm

urlpatterns = [
    path('', index, name='index'),
    path('total/', return_city_population, name='population'),
    path('profile/', profile, name='profile'),

    path('filter/', show_films, name='show_films'),
    path('create_film/', CreateFilm.as_view(), name='create_film')
]