import json
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse

from .models import Employee, Team
from .views import EmployeeViewSet, TeamViewSet


class EmployeeTestCase(APITestCase):

	@classmethod
	def setUp(self):
		self.team = Team.objects.create(name = 'TestTeam')
		self.employee = Employee.objects.create(first_name='Tony', last_name='Montana',email='tony@email.com')
		self.pk = 1



	def test_get_api(self):
		url = reverse('employee-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(Employee.objects.count(), 1)
		self.assertEqual(Employee.objects.get().email, 'tony@email.com')



	def test_create_api(self):
		url = reverse('employee-list')
		data = {
			    "first_name": "Test",
			    "last_name": "User",
			    "email": "test@email.com",
			    "team": 1
				}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Employee.objects.count(), 2)
		self.assertEqual(Employee.objects.all()[1].email, 'test@email.com')

	def test_put_or_delete(self):
		url = reverse('employee-detail', kwargs={'pk': self.pk})
		response = self.client.get(url)
		data = {
				"first_name" : "Godfrey",
				"team" : 1
				}
		response = self.client.patch(url, data = json.dumps(data), content_type = 'application/json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(Employee.objects.get().first_name, "Godfrey")
		self.client.delete(url)
		self.assertEqual(Employee.objects.count(), 0)



		
		

