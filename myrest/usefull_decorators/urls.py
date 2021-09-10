from django.urls import path

from usefull_decorators.views import my_view, my_view2, films

urlpatterns = [
    path('my_view/', my_view),
    path('my_view2/', my_view2),
    path('films/', films, name='films'),
]