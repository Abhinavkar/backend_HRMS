from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, status
from .models.bu_model import BusinessUnit
from .models.employee_model import EmployeeData
from .employee_management_serializer import EmployeeDataSerializer, BusinessUnitSerializer, EngagementDataSerializer,SkillDataSerializer, DepartmentDataSerializer,TechStackDataSerializer
from .models.engagment_model import Engagement
from .models.role_model import Role
from .models.skill_model import Skill
from .models.department_model import Department
from .employee_management_serializer import RoleDataSerializer
from .models.techstack_model import TechStack
from .employee_management_pagination import CustomPagination

################################################## GET API #############################################################



class EmployeeListView(APIView):
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination  # Use the custom pagination

    def get(self, request):
        employees = EmployeeData.objects.all()  # Fetch all employees

        # Paginate the queryset
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(employees, request)

        # Serialize the data
        serializer = EmployeeDataSerializer(result_page, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)

# class BusinessUnitListView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self,request):
#         business_unit = BusinessUnit.objects.all()
#         serializer = BusinessUnitSerializer(business_unit , many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

class BusinessUnitListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        business_units = BusinessUnit.objects.all()  # Fetch all business units

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(business_units, request)

        serializer = BusinessUnitSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class BusinessUnitDetailView(APIView):

    def get(self, request, id):
        try:
            business_unit = BusinessUnit.objects.get(pk=id)
            serializer = BusinessUnitSerializer(business_unit)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BusinessUnit.DoesNotExist:
            return Response({"error": f"Business Unit with {id} not found"}, status=status.HTTP_404_NOT_FOUND)



class EngagementListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        engagements = Engagement.objects.all()  # Fetch all engagements

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(engagements, request)

        serializer = EngagementDataSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


# class DepartmentListView (APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self,request):
#         departments = Department.objects.all() #fetch all the departments
#         serializer = DepartmentDataSerializer(departments, many=True)  # Serialize the data
#         return Response(serializer.data, status=status.HTTP_200_OK)

class DepartmentListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        departments = Department.objects.all()  # Fetch all departments

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(departments, request)

        serializer = DepartmentDataSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class DepartmentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            department = Department.objects.get(pk=id)  # Fetch department by ID
            serializer = DepartmentDataSerializer(department)  # Serialize the department data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

class SkillDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        skill= Skill.objects.get(pk=id)
        serializer = SkillDataSerializer(skill,id)
        return Response(serializer.data,status=status.HTTP_200_OK)


class SkillListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        skills = Skill.objects.all()  # Fetch all skills

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(skills, request)

        serializer = SkillDataSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


# class SkillListView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         skills= Skill.objects.all()
#         serializer  = SkillDataSerializer(skills,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)


class RoleListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        roles = Role.objects.all()  # Fetch all roles

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(roles, request)

        serializer = RoleDataSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

# class RoleListView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get (self ,request):
#         roles = Role.objects.all()
#         serializer  = RoleDataSerializer(roles,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)


class TechStackListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        techstacks = TechStack.objects.all()  # Fetch all tech stacks

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(techstacks, request)

        serializer = TechStackDataSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


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


class RoleCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RoleDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = DepartmentDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillsCreateView(APIView):
    def post(self,request):
        serializer = SkillDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechStackCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = TechStackDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





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



class RoleUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, name):
        role = Role.objects.get(id=id)
        serializer = RoleDataSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            department = Department.objects.get(pk=id)  # Fetch the department by ID
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentDataSerializer(department, data=request.data)  # Use the serializer for updating
        if serializer.is_valid():
            serializer.save()  # Save the updated data
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SkillsUpdateView(APIView):
    def put(self,request,id):
        try:
            skills= Skill.object.get(pk=id)
        except Skill.DoesNotExist:
            return Response({"error": "Business Unit not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SkillDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TechStackUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            Techstack = TechStack.objects.get(pk=id)  # Fetch the department by ID
        except Techstack.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentDataSerializer(Techstack, data=request.data)  #use for updating
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

class SkillsListDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request,id):
        try :
            skills = Skill.objects.get(pk=id)
        except Skill.DoesNotExist :
            return Response({"error":f"Skill {id}  does not exist " }, status=status.HTTP_404_NOT_FOUND)
        skills.delete()
        return Response({"message": "SKill deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class DepartmentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            department = Department.objects.get(pk=id)  # Fetch the department by ID
        except Department.DoesNotExist:
            return Response({"error": "Department does not exist"}, status=status.HTTP_404_NOT_FOUND)

        department.delete()  # Delete the department
        return Response({"message": "Department deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class RoleDeleteView(APIView):
    def delete(self, request, id):
        try:
            role = Role.objects.get(pk=id)
            role_name = role.name
            role.delete()
            custom_message = f"Details for role: {role.name}"
            return Response({
                "message": custom_message
            }, status=status.HTTP_204_NO_CONTENT)
        except Role.DoesNotExist:
            return Response({"error": "Role not found."}, status=status.HTTP_404_NOT_FOUND)


################################################## DELETE API ENDS  ###########################################################


