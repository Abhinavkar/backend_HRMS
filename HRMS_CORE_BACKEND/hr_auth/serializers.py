# serializers.py
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
