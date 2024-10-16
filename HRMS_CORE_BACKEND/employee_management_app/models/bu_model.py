from django.db import models
import uuid

class BusinessUnit(models.Model):
    bu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bu_name = models.CharField(max_length=100, verbose_name="Business Unit Name")

    def __str__(self):
        return self.bu_name
