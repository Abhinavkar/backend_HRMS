import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from employee_management_app.models.department_model import Department


class HRUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID field for id
    hr_personal_email_id = models.EmailField(unique=True, null=False, blank=False, editable=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_hr = models.BooleanField(default=True)

    def __str__(self):
        return self.username
