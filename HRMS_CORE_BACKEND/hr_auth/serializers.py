from rest_framework import serializers
from .models import HRUser

class HRUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = HRUser
        fields = ['username', 'password', 'email', 'department']  # Add other fields as needed

    def create(self, validated_data):
        user = HRUser(
            username=validated_data['username'],
            email=validated_data['email'],
            department=validated_data.get('department', ''),
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
