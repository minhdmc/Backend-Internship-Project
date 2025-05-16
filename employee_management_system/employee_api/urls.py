from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'performance', views.PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]