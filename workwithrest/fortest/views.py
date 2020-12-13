from importlib import import_module

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def brutal_funtion(request):
    return HttpResponse('For test purpose only!')


@method_decorator(csrf_exempt, 'dispatch')
class WorkWithUrls(View):
    def get(self, request, *args, **kwargs):
        return "not_implemented_response"

    def post(self, request, *args, **kwargs):
        return "not_implemented_response"

    def options(self, request, *args, **kwargs):
        uri = self.get_view_uri()
        uri = 'http://' + request.get_host() + uri

        allowed = self.get_allowed_methods()
        response_data = {'base': uri, 'allowed': allowed}

        return JsonResponse(response_data)

    def head(self, request, *args, **kwargs):
        return JsonResponse({})

    def get_view_uri(self):
        urls = import_module(__package__).urls.urlpatterns
        for url in urls:
            if hasattr(url.callback, 'view_class') and url.callback.view_class is self.__class__:
                return reverse(url.name)

    def get_allowed_methods(self):
        method_names = self.__class__._allowed_methods(self)
        method_names = map(str.lower, method_names)
        methods = []
        for name in method_names:
            if hasattr(self, name) and getattr(self, name).__name__ == name:
                methods.append(getattr(self, name))
        return methods