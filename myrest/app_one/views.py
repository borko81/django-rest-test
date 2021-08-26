from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .filters import FilmFilter
from .models import Country, City, Film
from .forms import FilmForm
from django.db.models import Sum, Count


def index(request):
    URL = 'http://api.ipstack.com/83.148.104.91?access_key=a7617ec806e6fb4e5fdc00f60a7cf57c'
    response = requests.get(URL)
    geodata = response.json()
    context = {
        'ip': geodata['ip'],
        'city': geodata['city']
    }
    return render(
        request, 'index.html',
        context
    )


def return_city_population(request):
    data = City.objects.values('country__name').annotate(total=Sum('population')).filter(total__gt=20000)
    data_two = City.objects.values('country__name').filter(name__startswith='P').annotate(city=Count('name'))
    return HttpResponse(data)


def profile(request):
    data ={
        'name': 'Borko',
        'age': '39',
        'email': 'korea600@abv.bg',
    }
    print(data)
    return JsonResponse(data, safe=False)


def show_films(request):
    obj = Film.objects.all()
    filter = FilmFilter(request.GET, queryset=obj)
    return render(request, 'filters.html', {'filter': filter, 'obj': obj})


class CreateFilm(CreateView):
    model = Film
    template_name = 'create_new_film.html'
    success_url = reverse_lazy('show_films')
    form_class = FilmForm