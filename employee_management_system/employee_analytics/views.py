from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Attendance, Performance
from django.db.models import Avg, Count
from django.contrib.auth.decorators import login_required
from employee_api.models import Department

@login_required
def dashboard(request):
    # Department-wise employee count
    department_stats = Department.objects.annotate(
        employee_count=Count('employees')
    ).values('name', 'employee_count')

    # Attendance statistics for the last 30 days
    attendance_stats = Attendance.objects.values('status').annotate(
        count=Count('id')
    ).order_by('status')

    # Performance rating distribution
    performance_stats = Performance.objects.values('rating').annotate(
        count=Count('id')
    ).order_by('rating')

    context = {
        'department_stats': list(department_stats),
        'attendance_stats': list(attendance_stats),
        'performance_stats': list(performance_stats),
    }
    
    return render(request, 'analytics/dashboard.html', context)

def employee_performance_data(request):
    performance_data = Performance.objects.values('employee__name').annotate(average_score=Avg('score'))
    return JsonResponse(list(performance_data), safe=False)

def employee_attendance_data(request):
    attendance_data = Attendance.objects.values('employee__name').annotate(total_days=Count('id'))
    return JsonResponse(list(attendance_data), safe=False)