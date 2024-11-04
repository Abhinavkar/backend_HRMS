from employee_management_app.models.bu_model import BusinessUnit as BusinessUnit
from rest_framework import serializers
from .project_management_app_models import Project # Adjust the import as needed

class ProjectSerializer(serializers.ModelSerializer):
    # Use a PrimaryKeyRelatedField for the business unit
    proj_business_unit = serializers.PrimaryKeyRelatedField(queryset=BusinessUnit.objects.all())

    class Meta:
        model = Project
        fields = '__all__'  # This now includes proj_business_unit directly

    def create(self, validated_data):
        # Create the Project instance
        project = Project.objects.create(**validated_data)
        return project
