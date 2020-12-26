from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

schema_view = get_swagger_view(title='Recipies API')

urlpatterns = [
    path('', include('accounts.urls')),
    path('api/', include('products.urls')),

    path('auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view, name='swagger'),
    path('swagger_new/', get_schema_view(
        title='Some title',
        description="Api description",
    ), name='openapi'),
]
