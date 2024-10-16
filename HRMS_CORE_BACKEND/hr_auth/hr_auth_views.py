from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import HRUserRegistrationSerializer

class HRUserRegistrationView(generics.CreateAPIView):
    serializer_class = HRUserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "HR user registered successfully."}, status=status.HTTP_201_CREATED)
