from django.urls import path
from .views import GroupListView, SimpleListView, RecepiListView

urlpatterns = [
    path('products/', SimpleListView.as_view(), name='products'),
    path('groups/', GroupListView.as_view(), name='groups'),
    path('recepi/', RecepiListView.as_view(), name='recepi'),

]
