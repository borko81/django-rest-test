from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll

MAX_OBJECTS = 20


def polls_list(request):
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"request": list(polls.values("question", "create_by__username", "pub_date"))}
    return JsonResponse(data)


def polls_detail(request,pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "result": {
            "question": poll.question,
            "create_by": poll.create_by.username,
            "pub_date": poll.pub_date
        }
    }
    return JsonResponse(data)