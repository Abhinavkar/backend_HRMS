
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("project_management_app.urls")),
    path('',include("employee_management_app.urls"))
]
