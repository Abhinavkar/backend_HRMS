from django.db import models
import uuid

class Engagement(models.Model):
    engagement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    engagement_type = models.CharField(max_length=100, verbose_name="Engagement Type")

    def __str__(self):
        return self.engagement_type
