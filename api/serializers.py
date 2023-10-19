from rest_framework import serializers

from .models import Team, Employee

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ('id', 'name')


class EmployeeSerializer(serializers.ModelSerializer):
	team_name = serializers.CharField(source='team.name', read_only=True)

	class Meta:
		model = Employee
		fields = ('id','first_name', 'last_name', 'email','team','team_name')
