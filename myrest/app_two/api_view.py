from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Groups, Simple
from .serializers import GroupSerializer, GroupAllSerializer, SimpleOnlySerializer


class GroupMixin:
    class Meta:
        abstract = True

    queryset = Groups.objects.all()
    serializer_class = GroupSerializer


class GroupList(GroupMixin, generics.ListCreateAPIView):
    pass


class GroupEdit(GroupMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class GroupCounter(APIView):

    def get(self, request):
        counter = Groups.objects.all().count()
        return Response({'total': counter})


class SimpleList(generics.ListCreateAPIView):
    queryset = Simple.objects.all()
    serializer_class = SimpleOnlySerializer


class SimpleEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simple.objects.all()
    serializer_class = SimpleOnlySerializer


class Meshanica(APIView):
    def get(self, request):
        groups = Groups.objects.all()
        data = GroupAllSerializer(groups, many=True).data
        return Response(data)
