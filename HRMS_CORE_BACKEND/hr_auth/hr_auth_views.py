from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import HRUserRegistrationSerializer, HRUserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings


class HRUserRegistrationView(generics.CreateAPIView):
    serializer_class = HRUserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "HR user registered successfully."}, status=status.HTTP_201_CREATED)


class HRUserLoginView(generics.GenericAPIView):
    serializer_class = HRUserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, generate tokens
            refresh = RefreshToken.for_user(user)

            # Set refresh token in a cookie
            response = Response({
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

            # Set HttpOnly cookie for refresh token
            response.set_cookie(
                key='refresh',
                value=str(refresh),
                httponly=True,
                secure=settings.SECURE_COOKIE,  # Use True in production
                samesite='Lax'
            )
            return response
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

    def post(self, request, *args, **kwargs):
        # Get refresh token from cookies
        refresh_token = request.COOKIES.get('refresh')
        if not refresh_token:
            return Response({"error": "Refresh token not found."}, status=status.HTTP_401_UNAUTHORIZED)

        # Prepare data for refreshing the token
        data = {"refresh": refresh_token}

        # Call the super method to perform token refresh
        response = super().post(request, data=data, *args, **kwargs)

        # Optionally, you might want to reset the refresh token cookie
        # response.set_cookie(key='refresh', value=refresh_token, httponly=True, secure=settings.SECURE_COOKIE, samesite='Lax')

        return response
