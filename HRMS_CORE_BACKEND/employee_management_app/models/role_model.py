from django.db import models
import uuid

class Role(models.Model):
    role_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=100, verbose_name="Role Name")

    def __str__(self):
        return self.role_name

