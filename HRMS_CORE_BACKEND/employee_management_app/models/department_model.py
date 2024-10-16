from django.db import models
import uuid

class Department(models.Model):
    dept_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dept_name = models.CharField(max_length=100, verbose_name="Department Name")
    dept_head = models.CharField(max_length=100, verbose_name="Department Head")

    def __str__(self):
        return self.dept_name
