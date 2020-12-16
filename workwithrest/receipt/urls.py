from django.urls import path
from .views import *

urlpatterns = [
    path('restaurant/', Restaurants.as_view()),
    path('restaurant/<str:restaurant_id>/', RestaurantDetail.as_view()),
]