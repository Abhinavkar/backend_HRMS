from django.db import models
import uuid
from project_management_app.project_management_app_models import Project
from .employee_model import EmployeeData
class EmployeeAndProject(models.Model):
    employee = models.ForeignKey(EmployeeData, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type_of_engagement = models.ForeignKey('Engagement', on_delete=models.SET_NULL, null=True)
    percentage_allocation = models.FloatField()
    role = models.CharField(max_length=100)
    allocation_date = models.DateTimeField()
    deallocation_date = models.DateTimeField(null=True, blank=True)
