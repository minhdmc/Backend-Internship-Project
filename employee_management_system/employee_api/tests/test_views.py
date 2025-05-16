import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from employee_api.models import Employee, Department

@pytest.mark.django_db
class TestEmployeeAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def department(self):
        return Department.objects.create(name="IT")

    @pytest.fixture
    def employee(self, department):
        return Employee.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            department=department,
            position="Developer",
            salary=50000
        )

    def test_list_employees(self, api_client, employee):
        url = reverse('employee-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_create_employee(self, api_client, department):
        url = reverse('employee-list')
        data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'department': department.id,
            'position': 'Designer',
            'salary': 45000
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Employee.objects.count() == 1

    def test_retrieve_employee(self, api_client, employee):
        url = reverse('employee-detail', kwargs={'pk': employee.id})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['first_name'] == 'John' 