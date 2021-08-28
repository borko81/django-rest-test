from django.urls import path
from .views import index, second


app_name = 'web'
urlpatterns = [
    path('', index, name='index'),
    path('second/<int:param>/', second, name='second'),
]