from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fortest/', include('fortest.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('maint/', include('maintenance.urls')),
    path('article/', include('articles.urls')),
    path('poll/', include('poll.urls')),

    path('rest/', include('receipt.urls')),
    path('company/', include('company.urls')),

    path('myauth/', include('rest_framework.urls')),
]
