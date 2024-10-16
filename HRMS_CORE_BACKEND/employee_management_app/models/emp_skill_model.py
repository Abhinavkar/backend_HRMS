from django.db import models

class EmployeeSkillRelation(models.Model):
    employee = models.ForeignKey('EmployeeData', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
