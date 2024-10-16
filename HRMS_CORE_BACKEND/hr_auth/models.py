import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class HRUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID field for id
    department = models.CharField(max_length=100, blank=True)  # Optional field for department
    is_hr = models.BooleanField(default=True)  # Field to specify if the user is an HR

    def __str__(self):
        return self.username
