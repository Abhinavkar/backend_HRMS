from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('hr_auth.hr_auth_urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # To get tokens (login)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # To refresh tokens
    path('employee/', include("employee_management_app.employee_management_urls")),  # Include your employee management app's URLs
    path('project/',include("project_management_app.project_management_app_urls"))
]

