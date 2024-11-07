from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .project_management_app_serializers import ProjectSerializer
from .project_management_app_models import Project


########################################### CREATE CLASS FOR ALL #############################
class ProjectManagementViewSet(APIView):
    permission_classes = [IsAuthenticated]
########################################### CREATE/POST ######################################
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()  # Save the new project
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######################################### GET ################################################
    def get(self, request):
        projects = Project.objects.all() # Fetch all the projects from the database
        serializer = ProjectSerializer(projects, many=True) # Serialize the projects using the ProjectSerializer
        return Response(serializer.data, status=status.HTTP_200_OK) #Return the serialized data in the response with status 200



####################################### PUT/PATCH #########################################

    def put(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'detail': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


