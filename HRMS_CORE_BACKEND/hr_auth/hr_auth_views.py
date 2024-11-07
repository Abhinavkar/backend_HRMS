from os import access
from struct import error

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import HRUserRegistrationSerializer, HRUserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from .utils.utils import send_hr_email

class HRUserRegistrationView(generics.CreateAPIView):
    serializer_class = HRUserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        # Validate and create the new user
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # Define email details
            subject = "Welcome to the HRMS Portal"
            username = serializer.validated_data.get('username', 'Your username')
            recipient_list = [serializer.validated_data['email']]
            message = (f"You have been registered as an HR user. You now have access to the portal.\n"
                       f"Your User ID is: {username}\n"
                       "Please log in with your credentials.")

            send_hr_email(subject, message, recipient_list)

            return Response({"message": "HR user registered successfully."}, status=status.HTTP_201_CREATED)

        except Exception as e:
             print(f"An error occurred: {e}")
             return Response({"error": "User registration failed. Please try again."}, status=status.HTTP_400_BAD_REQUEST)


class HRUserLoginView(generics.GenericAPIView):
    serializer_class = HRUserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = Response(status=status.HTTP_200_OK)
            response.set_cookie(
                key='refresh',  # Ensure this matches what you check for later
                value=str(refresh),
                httponly=True,
                secure=settings.SECURE_COOKIE,  # Use True in production
                samesite='Lax'
            )
            response.data = {
                'access': str(refresh.access_token),
            }
            return response

        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')
        if not refresh_token:
            return Response({"error": "Refresh token not found."}, status=status.HTTP_401_UNAUTHORIZED)
        data = {"refresh": refresh_token}
        try:
            response = super().post(request, data=data, *args, **kwargs)
            if response.status_code != 200:
                return Response(response.data, status=response.status_code)
            new_refresh_token = response.data.get('refresh')
            if new_refresh_token:
                response.set_cookie(
                    key='refresh',
                    value=new_refresh_token,
                    httponly=True,
                    secure=settings.SECURE_COOKIE,
                    samesite='Lax'
                )
            return response
        except Exception as e:
            print("Error during token refresh:", e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
