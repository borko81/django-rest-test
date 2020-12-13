from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Type
from .serializers import SerializerType


@csrf_exempt
def type_list(request):
    if request.method == 'GET':
        types = Type.objects.all()
        serializer = SerializerType(types, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerializerType(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def type_details(request, pk):
    try:
        t = Type.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerializerType(t, many=False)
        return JsonResponse(serializer.data, safe=False, status=200)