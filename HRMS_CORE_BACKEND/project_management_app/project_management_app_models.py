from django.db import models
import uuid
from employee_management_app.models.bu_model import BusinessUnit as BusinessUnit
class Project(models.Model):
    proj_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proj_name = models.CharField(max_length=100, verbose_name="Project Name")
    proj_requirement = models.TextField(verbose_name="Project Requirement")
    proj_lead = models.CharField(max_length=100, verbose_name="Project Lead")
    proj_manager = models.CharField(max_length=100, verbose_name="Project Manager")
    proj_tech_stack = models.CharField(max_length=100, verbose_name="Project Tech Stack")
    proj_status = models.CharField(max_length=100, verbose_name="Project Status")
    proj_client_details = models.TextField(verbose_name="Client Details")
    proj_estimate_date = models.DateTimeField()
    proj_start_date = models.DateTimeField()
    proj_end_date = models.DateTimeField()
    proj_created = models.DateTimeField(auto_now_add=True)
    proj_updated = models.DateTimeField(auto_now=True)
    proj_business_unit = models.ForeignKey('employee_management_app.BusinessUnit', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.proj_name




