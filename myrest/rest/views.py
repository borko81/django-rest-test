from django.http import HttpResponse
from rest_framework import viewsets

from rest.models import Person, Species
from rest.serializers import PersonSerializer, SpeciesSerializer


def index(request):
    return HttpResponse('This')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
