# employee_management_app/urls.py
from django.urls import path
from .views import set_cache, get_cache

urlpatterns = [
    path('set_cache/', set_cache, name='set_cache'),
    path('get_cache/', get_cache, name='get_cache'),
]
