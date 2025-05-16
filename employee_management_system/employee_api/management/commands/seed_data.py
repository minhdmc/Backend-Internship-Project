from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from datetime import timedelta
import random
from employee_api.models import Department, Employee, Attendance, Performance

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Create departments
        departments = [
            'Engineering',
            'Marketing',
            'Sales',
            'Human Resources',
            'Finance',
            'Operations',
            'IT',
            'Customer Support'
        ]
        
        department_objects = []
        for dept_name in departments:
            dept = Department.objects.create(
                name=dept_name,
                description=fake.text(max_nb_chars=200)
            )
            department_objects.append(dept)
            self.stdout.write(f'Created department: {dept_name}')

        # Create employees
        employees = []
        for _ in range(50):  # Create 50 employees
            employee = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                department=random.choice(department_objects),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=65),
                date_hired=fake.date_between(start_date='-5y', end_date='today')
            )
            employees.append(employee)
            self.stdout.write(f'Created employee: {employee.first_name} {employee.last_name}')

        # Create attendance records
        for employee in employees:
            # Create attendance records for the last 30 days
            for i in range(30):
                date = timezone.now().date() - timedelta(days=i)
                status = random.choices(
                    ['PRESENT', 'ABSENT', 'LATE'],
                    weights=[0.8, 0.1, 0.1]
                )[0]
                
                attendance = Attendance.objects.create(
                    employee=employee,
                    date=date,
                    status=status,
                    check_in=fake.time() if status != 'ABSENT' else None,
                    check_out=fake.time() if status != 'ABSENT' else None,
                    notes=fake.text(max_nb_chars=100) if status != 'PRESENT' else ''
                )
                self.stdout.write(f'Created attendance record for {employee} on {date}')

        # Create performance reviews
        for employee in employees:
            # Create 2-4 performance reviews per employee
            for _ in range(random.randint(2, 4)):
                review_date = fake.date_between(
                    start_date=employee.date_hired,
                    end_date='today'
                )
                performance = Performance.objects.create(
                    employee=employee,
                    review_date=review_date,
                    rating=random.randint(1, 5),
                    comments=fake.text(max_nb_chars=500),
                    goals_achieved=fake.text(max_nb_chars=300),
                    areas_for_improvement=fake.text(max_nb_chars=300)
                )
                self.stdout.write(f'Created performance review for {employee} on {review_date}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!')) 