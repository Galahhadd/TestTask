from django.contrib import admin

from .models import Team, Employee

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email', 'team']
