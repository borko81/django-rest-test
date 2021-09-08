from django.urls import path
from .apiviews import PollList, PollDetail, PollListAndCreate, PollDetailWithOther

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls_create/', PollListAndCreate.as_view(), name='polls_list_create'),

    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls_other/<int:pk>/', PollDetailWithOther.as_view(), name='polls_detail_with_other')
]