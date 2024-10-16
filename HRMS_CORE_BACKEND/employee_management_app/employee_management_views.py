from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class EmployeeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Example logic to return a list of employees
        employees = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]  # Replace with actual data retrieval logic
        return Response(employees, status=status.HTTP_200_OK)

class EmployeeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        # Example logic to return details of a specific employee by ID
        employee = {"id": id, "name": "John Doe"}  # Replace with actual data retrieval logic
        return Response(employee, status=status.HTTP_200_OK)

class EmployeeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Example logic to handle creating a new employee
        # You would normally deserialize request.data and save to the database
        return Response({"message": "New employee created"}, status=status.HTTP_201_CREATED)

class EmployeeUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        # Example logic to handle updating an employee
        # You would normally deserialize request.data and update the database entry
        return Response({"message": f"Employee with ID: {id} updated"}, status=status.HTTP_200_OK)

class EmployeeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        # Example logic to handle deleting an employee
        # You would normally delete the database entry
        return Response({"message": f"Employee with ID: {id} deleted"}, status=status.HTTP_204_NO_CONTENT)
