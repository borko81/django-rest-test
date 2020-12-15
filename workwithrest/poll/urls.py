from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PollList.as_view(), name='poll-list'),
    path('<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
]