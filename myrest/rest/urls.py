from django.urls import path
from .views import index, PersonViewSet, SpeciesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('person', PersonViewSet)
router.register('species', SpeciesViewSet)
