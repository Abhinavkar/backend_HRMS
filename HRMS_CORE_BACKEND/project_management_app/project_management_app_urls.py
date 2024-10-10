from django.urls import path

from .project_management_app_views import home_page

urlpatterns= [
    path("home/",home_page,name="home")
]