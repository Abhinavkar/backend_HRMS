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

        user = authenticate(request, username=username, password=password)

        if user is not None:

            refresh = RefreshToken.for_user(user)

            response = Response({
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)


            response.set_cookie(
                key='refresh',
                value=str(refresh),
                httponly=True,
                secure=settings.SECURE_COOKIE,
                samesite='Lax'
            )
            return response
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

    def post(self, request, *args, **kwargs):

        refresh_token = request.COOKIES.get('refresh')
        if not refresh_token:
            return Response({"error": "Refresh token not found."}, status=status.HTTP_401_UNAUTHORIZED)

        data = {"refresh": refresh_token}

        response = super().post(request, data=data, *args, **kwargs)
        response.set_cookie(key='refresh', value=refresh_token, httponly=True, secure=settings.SECURE_COOKIE, samesite='Lax')

        return response
