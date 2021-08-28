from django.urls import path
from .views import index, project_page

app_name='projects'
urlpatterns = [
    path('', index, name='start'),
    path('project_page/<int:pk>/', project_page, name='project_page')
]
