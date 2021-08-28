from django.shortcuts import render


def index(request):
    my_variable = 'Hellow worlds'
    age = 40
    attay_cityes = [ "Paris", "London", "Washington" ]
    contex = {
        'my_variable': my_variable,
        'attay_cityes': attay_cityes,
        'age': age,
        'title': 'Index page'
    }
    return render(request, 'web/web_index.html', contex)


def second(request, param):
    return render(request, 'web/second_page.html', {'param': param})