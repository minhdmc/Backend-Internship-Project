from django.test import TestCase
from .models import Employee, Department

class EmployeeAnalyticsTests(TestCase):

    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.employee = Employee.objects.create(
            name="John Doe",
            department=self.department,
            position="Manager",
            salary=60000
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, "John Doe")
        self.assertEqual(self.employee.department.name, "HR")
        self.assertEqual(self.employee.position, "Manager")
        self.assertEqual(self.employee.salary, 60000)

    def test_department_association(self):
        self.assertIn(self.employee, self.department.employee_set.all())

    def test_employee_str(self):
        self.assertEqual(str(self.employee), "John Doe")