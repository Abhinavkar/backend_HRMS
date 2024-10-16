from django.db import models

class EmployeeProjectRelation(models.Model):
    employee = models.ForeignKey('EmployeeData', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    engagement = models.ForeignKey('Engagement', on_delete=models.CASCADE)
    engagement_percentage = models.FloatField()
