from django.db import models
import uuid

class TechStack(models.Model):
    techstack_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    techstack_name = models.CharField(max_length=100, verbose_name="Tech Stack Name")

    def __str__(self):
        return self.techstack_name
