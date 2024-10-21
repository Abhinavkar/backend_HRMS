from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Project work buddy ",
        default_version='v1',
        description="Project Workbuddy api config ",
        contact=openapi.Contact(email="abhinav.kar@vvdntech.in"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('hr_auth.hr_auth_urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # To get tokens (login)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # To refresh tokens
    path('employee/', include("employee_management_app.employee_management_urls")),  # Include your employee management app's URLs
    path('project/',include("project_management_app.project_management_app_urls")),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

