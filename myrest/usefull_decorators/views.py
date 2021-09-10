import time

from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Films
from .filters import FilmFilter


def super_user_only(function):

    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return function(request, *args, **kwargs)

    return _inner


def decorator_factory(group_names):
    def user_in_group_only(function):

        def _inner(request, *args, **kwargs):
            if request.user.username not in group_names:
                raise PermissionDenied
            return function(request, *args, **kwargs)

        return _inner
    return user_in_group_only


def timeit(function):
    def timer(*args, **kwargs):
        begin = time.time()
        result = function(*args, **kwargs)
        print(time.time() - begin)
        return result
    return timer


@login_required()
def my_view(request):
    return HttpResponse('Login required')


@decorator_factory(['admin', 'root', 'borko'])
@timeit
def my_view2(request):
    return HttpResponse('Login required')


def films(request):
    obj = Films.objects.all()
    content = {'films': obj, 'filter': FilmFilter(request.GET, queryset=obj)}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        content = {
            'name': name,
            'price': price
        }
        try:
            Films.objects.create(**content)
        except Exception as e:
            print(e)
        return redirect('films')

    return render(request, 'deco/index.html', content)

