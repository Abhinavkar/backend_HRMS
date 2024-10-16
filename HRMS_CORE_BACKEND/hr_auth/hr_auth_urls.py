from django.urls import path
from .hr_auth_views import HRUserRegistrationView  # Correctly import from hr_auth_views

urlpatterns = [
    path('register/', HRUserRegistrationView.as_view(), name='hr_user_register'),  # Registration URL
]
