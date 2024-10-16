from django.db import models
import uuid

class Skill(models.Model):
    skills_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skills_name = models.CharField(max_length=100, verbose_name="Skill Name")

    def __str__(self):
        return self.skills_name
