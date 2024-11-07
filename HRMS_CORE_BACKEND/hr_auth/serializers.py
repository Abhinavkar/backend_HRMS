# serializers.py
from rest_framework import serializers
from .models import HRUser
from employee_management_app.models.employee_model import EmployeeData
class HRUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = HRUser.objects.filter(username=username).first()
            if user and user.check_password(password):
                return attrs  # Return validated data if user exists and password is correct
            else:
                raise serializers.ValidationError("Invalid username or password.")
        raise serializers.ValidationError("Must include 'username' and 'password'.")

class HRUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = HRUser
        fields = ['username', 'password', 'email', 'department']  # Add other fields as needed

    def create(self, validated_data):
        user = HRUser(
            username=validated_data['username'],
            hr_personal_email_id=validated_data['email'],
            department=validated_data.get('department'),
            is_hr=True  # Ensure this is an HR user
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = EmployeeData
        fields = ['emp_first_name', 'emp_last_name', 'emp_personal_email', 'emp_department', 'password']

    def create(self, validated_data):
        # Create the employee user account
        user = HRUser(
            username=validated_data['emp_personal_email'],  # Use email as username or set as needed
            hr_personal_email_id=validated_data['emp_personal_email'],
            is_hr=False  # Set is_hr to False for regular employees
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create the EmployeeData entry
        employee = EmployeeData(
            emp_username=user,
            emp_first_name=validated_data['emp_first_name'],
            emp_last_name=validated_data['emp_last_name'],
            emp_personal_email=validated_data['emp_personal_email'],
            emp_department=validated_data.get('emp_department')
        )
        employee.save()
        return employee
