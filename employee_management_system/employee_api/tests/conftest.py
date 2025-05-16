import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from employee_api.models import Department, Employee

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def admin_user():
    return User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )

@pytest.fixture
def authenticated_client(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    return api_client

@pytest.fixture
def department():
    return Department.objects.create(name="IT")

@pytest.fixture
def employee(department):
    return Employee.objects.create(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        department=department,
        position="Developer",
        salary=50000
    ) 