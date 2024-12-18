from django.urls import path
from rest_framework.permissions import IsAuthenticated
from . import employee_management_views as views



urlpatterns = [
    # EMPLOYEE URLS
    path('list/', views.EmployeeListView.as_view(permission_classes=[IsAuthenticated]), name='employee_list'),
    # path('detail/<int:id>/', views.EmployeeDetailView.as_view(permission_classes=[IsAuthenticated]), name='employee_detail'),
    # path('create/', views.EmployeeCreateView.as_view(permission_classes=[IsAuthenticated]), name='employee_create'),
    path('update/<int:id>/', views.EmployeeUpdateView.as_view(permission_classes=[IsAuthenticated]), name='employee_update'),
    # path('delete/<int:id>/', views.EmployeeDeleteView.as_view(permission_classes=[IsAuthenticated]), name='employee_delete'),

    # BUSINESS UNIT URLS
    path("get-business-unit/", views.BusinessUnitListView.as_view(permission_classes=[IsAuthenticated]), name= "business_unit_details"),
    path('create-business-unit/',views.BusinessUnitCreateView.as_view(permission_classes=[IsAuthenticated]),name="business_unit_create"),
    path("update-business-unit/<uuid:id>/", views.BusinessUnitUpdateView.as_view(permission_classes=[IsAuthenticated]),name="business_unit_update"),
    path("delete-business-unit/<uuid:id>/", views.BusinessUnitDeleteView.as_view(permission_classes=[IsAuthenticated]),name="business_unit_delete"),
    path("get-business-unit/<uuid:id>/",views.BusinessUnitDetailView.as_view(permission_classes=[IsAuthenticated]),name="business_unit_details_id"),

    # Engagement Urls
    path("get-engagement-type-list/",views.EngagementListView.as_view(permission_classes=[IsAuthenticated]), name="engagement_details"),
    path("create-engagement-type/",views.EngagementCreateView.as_view(permission_classes=[IsAuthenticated]),name="engagement_create"),

    #ROLE URLS
    path("get-roles-list/" ,views.RoleListView.as_view(permission_classes = [IsAuthenticated]) , name = "roles_details"),
    path("create-roles/",views.RoleCreateView.as_view(permission_classes = [IsAuthenticated] ) ,name ="roles_details"),
    path("update-roles/<uuid:id>/", views.RoleUpdateView.as_view(permission_classes=[IsAuthenticated]), name="roles_details"),
    path("delete-roles/<uuid:id>/", views.RoleDeleteView.as_view(permission_classes=[IsAuthenticated]), name="roles_details"),

    # SKills Api
    path("get-skills-list/",views.SkillListView.as_view(permission_classes=[IsAuthenticated]),name="skills_details"),
    path("get-skills-list/<uuid:id>",views.SkillDetailView.as_view(permission_classes=[IsAuthenticated]),name="skills_details_by_id"),
    path("create-skills/",views.SkillsCreateView.as_view(permission_classes=[IsAuthenticated]),name="create_skills"),
    path("delete-skills/<uuid:id>/",views.SkillsListDeleteView.as_view(permission_classes=[IsAuthenticated]),name="delete_skills"),
    path("update-skills/<uuid:id>/",views.SkillsUpdateView.as_view(permission_classes=[IsAuthenticated]),name="update_skills"),
    path("update-skills/<uuid:id>/",views.SkillsUpdateView.as_view(permission_classes=[IsAuthenticated]),name="update_skills"),
    path("get-skills-list/",views.SkillListView.as_view(permission_classes=[IsAuthenticated]),name="skills_deltails"),

    #DEPARTMENT UNIT URLS
    path("get-department-list/", views.DepartmentListView.as_view(),name="DepartmentListView"),
    path("get-department-list/<uuid:id>/", views.DepartmentDetailView.as_view(permission_classes=[IsAuthenticated]),name="DepartmentListView"),
    path("create-department/", views.DepartmentCreateView.as_view(permission_classes=[IsAuthenticated]), name="DepartmentCreateView"),
    path("update-department/<uuid:id>/", views.DepartmentUpdateView.as_view(permission_classes=[IsAuthenticated]), name="DepartmentUpdateView"),
    path("delete-department/<uuid:id>/", views.DepartmentDeleteView.as_view(permission_classes=[IsAuthenticated]), name="DepartmentDeleteView"),

    #TECHSTACK API
    path("get-TechStack-list/", views.TechStackListView.as_view(permission_classes=[IsAuthenticated]), name='TechStackListView'),
    path("create-techstack/", views.TechStackCreateView.as_view(permission_classes=[IsAuthenticated]), name="TechStackCreateView"),


]
