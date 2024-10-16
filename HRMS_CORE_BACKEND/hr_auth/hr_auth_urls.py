# hr_auth_urls.py

from django.urls import path
from .hr_auth_views import HRUserRegistrationView, HRUserLoginView ,CustomTokenRefreshView # Import the login view

urlpatterns = [
    path('register/', HRUserRegistrationView.as_view(), name='hr_user_register'),  # Registration URL
    path('login/', HRUserLoginView.as_view(), name='hr_user_login'),  # Login URL
    path("token_refresh",CustomTokenRefreshView.as_view(), name="refreshtoken")
]
