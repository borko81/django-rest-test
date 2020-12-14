from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Type, Employee, Problem
from .serializers import SerializerType, SerializerEmployee, SerializerProblem

'''
http --json PUT :8000/maint/employee/2/ name="Employee one" email="abv@abv.bg"
'''

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

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerializerType(t, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        t.delete()
        return HttpResponse(status=204)


@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = SerializerEmployee(emp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerializerEmployee(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employee_detail(request, pk):
    try:
        e = Employee.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerializerEmployee(e, many=False)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerializerEmployee(e, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        e.delete()
        return HttpResponse(status=204)


def problem_list(request):
    if request.method == 'GET':
        problem = Problem.objects.all()
        serializer = SerializerProblem(problem, many=True)
        return JsonResponse(serializer.data, safe=False)
