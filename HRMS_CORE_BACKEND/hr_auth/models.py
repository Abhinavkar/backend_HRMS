from django.db import models
from django.contrib.auth.models import AbstractUser

class HRUser(AbstractUser):
    """
    Custom HR user model extending the built-in AbstractUser.
    You can add additional fields for HR-specific requirements here.
    """
    department = models.CharField(max_length=100, blank=True)  # Optional field for department
    is_hr = models.BooleanField(default=True)  # Field to specify if the user is an HR

    def __str__(self):
        return self.username
