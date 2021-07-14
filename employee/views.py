from django.shortcuts import render, redirect
from django.conf import settings
from .forms import EmployeeForm

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .filters import EmployeeFilter
from .decorators import allowUser

@login_required(login_url="/login/")
def employee_list(request):
    employee_list = settings.AUTH_USER_MODEL.objects.all()

    myFilter = EmployeeFilter(request.GET, queryset=employee_list)
    employee_list = myFilter.qs

    context = {'employee_list': employee_list, 'myFilter': myFilter}
    
    return render(request, "ui-tables.html", context)

@login_required(login_url="/login/")
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = settings.AUTH_USER_MODEL.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = settings.AUTH_USER_MODEL.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/list')
        

@login_required(login_url="/login/")
def employee_delete(request,id):
    employee = settings.AUTH_USER_MODEL.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
