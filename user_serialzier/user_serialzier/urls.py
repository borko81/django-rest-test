from django import urls
from django.contrib import admin
from django.urls import path, include
import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('rest_framework.urls')),
    path('app01/', include('app01.urls')),
]
