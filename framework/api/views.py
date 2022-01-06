from framework.models import Employee
from framework.api.serializer import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EmployeeViewSet(viewsets.ModelViewSet):
 queryset = Employee.objects.all()
 serializer_class = EmployeeSerializer
 authentication_classes = [SessionAuthentication]
 permission_classes = [IsAuthenticatedOrReadOnly]