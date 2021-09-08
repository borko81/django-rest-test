from django.urls import path
from .api_view import GroupList, GroupEdit, GroupCounter, SimpleList, SimpleEdit, Meshanica

urlpatterns = [
    path('group/', GroupList.as_view(), name='group_list'),
    path('group/<int:pk>/', GroupEdit.as_view(), name='group_edit'),
    path('group_count/', GroupCounter.as_view(), name='group_count'),

    path('simple/', SimpleList.as_view(), name='simple_list'),
    path('simple/<int:pk>/', SimpleEdit.as_view(), name='simple_edit'),

    path('all/', Meshanica.as_view(), name='all'),
]