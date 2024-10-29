from .models.department_model import Department
from .models.employee_model import EmployeeData
from .models.bu_model import BusinessUnit
from .models.engagment_model import Engagement
from .models.role_model import Role
from .models.skill_model import Skill
from .models.techstack_model import TechStack
from rest_framework import serializers
class EmployeeDataSerializer(serializers.ModelSerializer):
    emp_skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    emp_tech_stacks = serializers.PrimaryKeyRelatedField(queryset=TechStack.objects.all(), many=True)
    emp_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    emp_business_unit = serializers.PrimaryKeyRelatedField(queryset=BusinessUnit.objects.all(), allow_null=True)
    emp_type_of_engagement = serializers.PrimaryKeyRelatedField(queryset=Engagement.objects.all(), allow_null=True)

    class Meta:
        model = EmployeeData
        fields = [
            'emp_id', 'emp_first_name', 'emp_last_name', 'emp_personal_email', 'emp_phone_number',
            'emp_permanent_address', 'emp_current_address', 'emp_blood_group', 'emp_reporting_manager',
            'emp_tech_group', 'emp_department', 'emp_date_of_joining', 'emp_dob', 'emp_designation',
            'emp_years_of_experience', 'emp_ctc_salary', 'emp_tech_stacks', 'emp_job_location',
            'emp_base_location', 'emp_gender', 'emp_allocation_status', 'emp_business_unit',
            'emp_type_of_engagement', 'emp_location_hr', 'emp_skills'
        ]


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

class TechStackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = ['techstack_id', 'techstack_name']  # Replace with actual fields in your model
