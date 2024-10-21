from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models.bu_model import BusinessUnit
from .models.employee_model import EmployeeData
from .emp_serializer import EmployeeDataSerializer, BusinessUnitSerializer, EngagementDataSerializer
from .models.engagment_model import Engagement


################################################## GET API #############################################################

class EmployeeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = EmployeeData.objects.all()  # Fetch all employees
        serializer = EmployeeDataSerializer(employees, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmployeeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        # Example logic to return details of a specific employee by ID
        employee = {"id": id, "name": "John Doe"}  # Replace with actual data retrieval logic
        return Response(employee, status=status.HTTP_200_OK)

class BusinessUnitListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        business_unit = BusinessUnit.objects.all()
        serializer = BusinessUnitSerializer(business_unit , many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class EngagementListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        engagement=Engagement.objects.all()
        serializer=EngagementDataSerializer(engagement,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


################################################## GET API ENDS ########################################################

################################################## CREATE / POST  API ##################################################


class EmployeeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Example logic to handle creating a new employee
        # You would normally deserialize request.data and save to the database
        return Response({"message": "New employee created"}, status=status.HTTP_201_CREATED)



class BusinessUnitCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BusinessUnitSerializer(data=request.data)  # Deserialize and validate data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EngagementCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = EngagementDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





################################################## CREATE / POST API ENDS ##############################################



################################################## PUT API #############################################################


class EmployeeUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        # Example logic to handle updating an employee
        # You would normally deserialize request.data and update the database entry
        return Response({"message": f"Employee with ID: {id} updated"}, status=status.HTTP_200_OK)



class BusinessUnitUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            business_unit = BusinessUnit.objects.get(pk=id)
        except BusinessUnit.DoesNotExist:
            return Response({"error": "Business Unit not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BusinessUnitSerializer(business_unit, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the updated data
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################## PUT API ENDS ########################################################



################################################## PATCH API ###########################################################

################################################## PATCH API ###########################################################


################################################## DELETE API ###########################################################
class BusinessUnitDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request,id):
        try :
            business_unit = BusinessUnit.objects.get(pk=id)
        except BusinessUnit.DoesNotExist :
            return Response({"error":"Business Unit does not exist " }, status=status.HTTP_404_NOT_FOUND)

        business_unit.delete()
        return Response({"message": "Business Unit deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



################################################## DELETE API ###########################################################