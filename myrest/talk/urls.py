from django.urls import path

from talk.views import home, post_collection, get_concrete_post, index

urlpatterns = [
    path('', home, name='home'),
    path('posta_all/', post_collection, name='post_collection'),
    path('post/<int:pk>/', get_concrete_post, name='get_concrete_post'),

    path('js_result/', index, name='js_result')
]