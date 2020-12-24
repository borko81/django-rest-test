from django.urls import path
from .views import GroupListView, SimpleListView, RecepiListView, RecepiDetails, RecepiIng, RecepiIngDetail

urlpatterns = [
    path('products/', SimpleListView.as_view(), name='products'),
    path('groups/', GroupListView.as_view(), name='groups'),
    path('recepi/', RecepiListView.as_view(), name='recepi'),
    path('recepi/<int:pk>/', RecepiDetails.as_view(), name='recepi_detail'),
    path('recepiing/', RecepiIng.as_view(), name='recepiing'),
    path('recepiing/<int:pk>/', RecepiIngDetail.as_view(), name='recepiing_detail'),
]
