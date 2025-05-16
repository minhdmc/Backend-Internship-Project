from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee, Department

class EmployeeAPITests(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            department=self.department
        )

    def test_employee_list(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_employee_detail(self):
        response = self.client.get(reverse('employee-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.employee.name)

    def test_create_employee(self):
        data = {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "department": self.department.id
        }
        response = self.client.post(reverse('employee-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_update_employee(self):
        data = {
            "name": "John Updated",
            "email": "john.updated@example.com",
            "department": self.department.id
        }
        response = self.client.put(reverse('employee-detail', args=[self.employee.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, "John Updated")

    def test_delete_employee(self):
        response = self.client.delete(reverse('employee-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)