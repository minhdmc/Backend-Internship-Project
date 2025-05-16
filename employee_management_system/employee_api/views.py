from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Employee, Department, Attendance, Performance
from .serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    AttendanceSerializer,
    PerformanceSerializer
)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']
    ordering_fields = ['first_name', 'last_name', 'date_hired']

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'status', 'date']
    search_fields = ['employee__first_name', 'employee__last_name']
    ordering_fields = ['date', 'status']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'rating', 'review_date']
    search_fields = ['employee__first_name', 'employee__last_name', 'comments']
    ordering_fields = ['review_date', 'rating']

def employee_analytics(request):
    # Placeholder for future analytics view
    return Response({"message": "Employee analytics will be implemented here."})