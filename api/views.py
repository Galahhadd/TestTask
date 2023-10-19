from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import EmployeeSerializer, TeamSerializer
from .models import Team, Employee


@api_view(['GET'])
def ApiLinks(request):

    api_urls = {

        'Show list of Employees or create a new one': '/api/employee/',

        'Update or Delete Employee': '/api/employee/<int:pk>/',

        'Show list of Teams or create a new one': '/api/team/',

        'Update or Delete Team': '/api/team/<int:pk>/'

    }
 
    return Response(api_urls)

class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer



