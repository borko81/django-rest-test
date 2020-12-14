from django.urls import path
from .views import type_list, type_details, employee_detail, employee_list, problem_list

urlpatterns = [
    path('', type_list, name='type_list'),
    path('<int:pk>/', type_details, name='type_details'),

    path('employee/', employee_list, name='all-employee'),
    path('employee/<int:pk>/', employee_detail, name='emp-detail'),

    path('problem/', problem_list, name='all-problem')
]
