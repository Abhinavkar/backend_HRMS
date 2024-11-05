from django.urls import path
from .project_management_app_views import ProjectManagementViewSet

urlpatterns = [
    path('create-project/', ProjectManagementViewSet.as_view(), name='project_create'),  # Define the path for creating projects
    path('get-projects/', ProjectManagementViewSet.as_view(), name='project-list'),  # Endpoint to get all projects
    path('put-projects/<int:pk>/', ProjectManagementViewSet.as_view(), name='project-detail'),  # PUT method to update a specific project
]

