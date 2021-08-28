from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Developer, Project, UserProfile


def index(request):
    obj = UserProfile.objects.all()
    project = Project.objects.filter(client_name='TEstov account').get()
    return render(request, 'project/dev.html', {'obj': obj, 'project': project})


def project_page(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project/index_project.html', {'project': project})