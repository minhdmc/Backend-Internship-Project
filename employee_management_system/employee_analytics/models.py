from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # e.g., 'Present', 'Absent'

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()  # e.g., 1 to 5

    def __str__(self):
        return f"{self.employee} - {self.review_date} - Score: {self.score}"