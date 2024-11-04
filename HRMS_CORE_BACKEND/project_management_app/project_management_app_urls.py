from django.urls import path
from .project_management_app_views import ProjectManagementViewSet

urlpatterns = [
    path('create-project/', ProjectManagementViewSet.as_view(), name='project_create'),  # Define the path for creating projects
]
