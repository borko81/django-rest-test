from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', poll_list, name='poll-list'),
    path('<int:pk>/', poll_detail, name='poll-detail'),
]