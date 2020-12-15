from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

from datetime import datetime
from .serializers import *

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

