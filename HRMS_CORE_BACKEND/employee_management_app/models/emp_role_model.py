from django.db import models

class EmployeeRoleRelation(models.Model):
    employee = models.ForeignKey('EmployeeData', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
