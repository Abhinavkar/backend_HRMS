from django.db import models

class PROJECT(models.Model):
    project_name = models.CharField(max_length=30)
    project_requirement = models.CharField(max_length=1000)
    project_lead = models.CharField(max_length=50)
    project_manager = models.CharField(max_length=50)
    project_tech_stack = models.CharField(max_length=50)
    project_status = models.CharField(max_length=50)
    project_client_details = models.CharField(max_length=1000)
    project_business_unit = models.CharField(max_length=50)
    project_estimate_date = models.DateTimeField()
    project_start_date = models.DateTimeField()
    project_end_date = models.DateTimeField()
    project_uuid = models.IntegerField(primary_key=True)
    project_created = models.DateTimeField(auto_now_add=True)
    project_updated = models.DateTimeField(auto_now=True)
