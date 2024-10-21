from django.urls import path
from rest_framework.permissions import IsAuthenticated
from . import employee_management_views as views  # Importing views

urlpatterns = [
    path('list/', views.EmployeeListView.as_view(permission_classes=[IsAuthenticated]), name='employee_list'),
    path('detail/<int:id>/', views.EmployeeDetailView.as_view(permission_classes=[IsAuthenticated]), name='employee_detail'),
    path('create/', views.EmployeeCreateView.as_view(permission_classes=[IsAuthenticated]), name='employee_create'),
    path('update/<int:id>/', views.EmployeeUpdateView.as_view(permission_classes=[IsAuthenticated]), name='employee_update'),
    path('delete/<int:id>/', views.EmployeeDeleteView.as_view(permission_classes=[IsAuthenticated]), name='employee_delete'),
# path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
