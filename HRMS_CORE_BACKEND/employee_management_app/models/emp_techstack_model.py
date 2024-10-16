from django.db import models

class EmployeeTechStackRelation(models.Model):
    employee = models.ForeignKey('EmployeeData', on_delete=models.CASCADE)
    tech_stack = models.ForeignKey('TechStack', on_delete=models.CASCADE)
