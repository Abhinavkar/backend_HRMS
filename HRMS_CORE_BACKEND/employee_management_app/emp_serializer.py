from rest_framework import serializers

from .models.department_model import Department
from .models.employee_model import EmployeeData
from .models.bu_model import BusinessUnit
from .models.engagment_model import Engagement
from .models.role_model import Role
from .models.skill_model import Skill


class EmployeeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeData
        fields = [
            'emp_id', 'emp_first_name', 'emp_last_name', 'emp_personal_email',
            'emp_phone_number', 'emp_designation', 'emp_department', 'emp_skills',
            'emp_blood_group', 'emp_gender', 'emp_date_of_joining'
        ]  # Include any other fields you want to expose in the API


class BusinessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = ['bu_id', 'bu_name']


class EngagementDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = ['engagement_id',"engagement_type"]



class SkillDataSerializer(serializers.ModelSerializer):
    class Meta :
        model=Skill
        fields= ['skills_id','skills_name']


class DepartmentDataSerializer(serializers.ModelSerializer):
    class Meta :
        model=Department
        fields = ['dept_id','dept_name','dept_head']



class RoleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id' ,'role_name']