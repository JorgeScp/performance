from .models import *
import django_filters
from django_filters import CharFilter

class EmployeeFilter(django_filters.FilterSet):
    name = CharFilter(field_name="fullname", lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ''



