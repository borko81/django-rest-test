from . import views
from . import  myview

from django.urls import path

urlpatterns = [
    path('test/', views.WorkWithUrls.as_view())
]
