from django.db import models


class Team(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Employee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(unique=True, max_length=255)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.email
