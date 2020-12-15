from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import *
from .serializers import *

from datetime import datetime


# Without use DRF

def poll_list(request):
    MAX_OBJECT = 5
    polls = Poll.objects.all()[:MAX_OBJECT]
    data = {"result": list(polls.values('id', "question", "created_by"))}
    return JsonResponse(data, status=200)


def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"result": {
        "question": poll.question,
        "created_by": {
            "user_name": poll.created_by.username,
            "user_id": poll.created_by.id,
        },
        "pub_date": poll.pub_date.strftime("%d.%m.%Y"),
    }}
    return JsonResponse(data, status=200)


# With DRF

def convert_date_format(date):
    return date.strftime("%d.%m.%Y")


class PollList(APIView):
    def get(self, request):
        poll = Poll.objects.all()
        data = PollSerializer(poll, many=True).data
        return Response(data)


# class PollDetailView(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         poll.pub_date = convert_date_format(poll.pub_date)
#         data = PollSerializer(poll).data
#         return Response(data)


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
