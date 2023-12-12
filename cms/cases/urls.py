from django.urls import path
from .views import case_list, search_cases, case_detail
from .views import login_view, logout_view, case_list, add_case

urlpatterns = [
    path('', case_list, name='case_list'),
    path('search/', search_cases, name='search_cases'),
    path('case/<int:pk>/', case_detail, name='case_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_case/', add_case, name='add_case'),

    # Add more URL patterns as needed
]
