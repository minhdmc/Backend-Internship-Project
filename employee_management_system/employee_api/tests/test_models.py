import pytest
from django.core.exceptions import ValidationError
from employee_api.models import Employee, Department

@pytest.mark.django_db
class TestEmployeeModel:
    def test_create_employee(self):
        department = Department.objects.create(name="IT")
        employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            department=department,
            position="Developer",
            salary=50000
        )
        assert employee.first_name == "John"
        assert employee.last_name == "Doe"
        assert str(employee) == "John Doe"

    def test_employee_email_validation(self):
        department = Department.objects.create(name="IT")
        with pytest.raises(ValidationError):
            Employee.objects.create(
                first_name="John",
                last_name="Doe",
                email="invalid-email",
                department=department,
                position="Developer",
                salary=50000
            )

@pytest.mark.django_db
class TestDepartmentModel:
    def test_create_department(self):
        department = Department.objects.create(name="HR")
        assert department.name == "HR"
        assert str(department) == "HR" 