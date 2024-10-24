from django.urls import path
from rest_framework.permissions import IsAuthenticated
from . import employee_management_views as views  # Importing views

urlpatterns = [
    # EMPLOYEE URLS
    path('list/', views.EmployeeListView.as_view(permission_classes=[IsAuthenticated]), name='employee_list'),
    path('detail/<int:id>/', views.EmployeeDetailView.as_view(permission_classes=[IsAuthenticated]), name='employee_detail'),
    path('create/', views.EmployeeCreateView.as_view(permission_classes=[IsAuthenticated]), name='employee_create'),
    path('update/<int:id>/', views.EmployeeUpdateView.as_view(permission_classes=[IsAuthenticated]), name='employee_update'),
    # path('delete/<int:id>/', views.EmployeeDeleteView.as_view(permission_classes=[IsAuthenticated]), name='employee_delete'),


    # BUSINESS UNIT URLS
    path("get-business-unit/", views.BusinessUnitListView.as_view(permission_classes=[IsAuthenticated]), name= "business_unit_details"),
    path('create-business-unit/',views.BusinessUnitCreateView.as_view(permission_classes=[IsAuthenticated]),name="business_unit_create"),
    path("update-business-unit/<uuid:id>/", views.BusinessUnitUpdateView.as_view(permission_classes=[IsAuthenticated]),name="business_unit_update"),
    path("delete-business-unit/<uuid:id>/", views.BusinessUnitDeleteView.as_view(permission_classes=[IsAuthenticated]),name="business_unit_delete"),

    path("get-engagement-type-list/",views.EngagementListView.as_view(permission_classes=[IsAuthenticated]), name="engagement_details"),
    path("create-engagement-type/",views.EngagementCreateView.as_view(permission_classes=[IsAuthenticated]),name="engagement_create")


]
