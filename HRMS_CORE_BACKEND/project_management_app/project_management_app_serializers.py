# project_management_app_serializers.py

from rest_framework import serializers
from .project_management_app_models import Project
from employee_management_app.employee_management_serializer import BusinessUnitSerializer

class ProjectSerializer(serializers.ModelSerializer):
    proj_bu_serializer = BusinessUnitSerializer()
    class Meta:
        model = Project
        fields = '__all__'
