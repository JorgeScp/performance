from django.shortcuts import render, redirect
from .models import Contracts
from .forms import ContractsForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
#from .filters import EmployeeFilter

@login_required(login_url="/login/")
def contracts_list(request):
    contracts_list = Contracts.objects.all()

    # myFilter = EmployeeFilter(request.GET, queryset=contracts_list)
    # contracts_list = myFilter.qs

    # context = {'contracts_list': contracts_list, 'myFilter': myFilter}
    context = {'contracts_list': contracts_list}
    
    return render(request, "contracts_list.html", context)

@login_required(login_url="/login/")
def contracts_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ContractsForm()
        else:
            employee = Contracts.objects.get(pk=id)
            form = ContractsForm(instance=employee)
        return render(request, "employee_form.html", {'form': form})
    else:
        if id == 0:
            form = ContractsForm(request.POST)
        else:
            employee = Contracts.objects.get(pk=id)
            form = ContractsForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/contracts_list')

@login_required(login_url="/login/")
def contracts_delete(request,id):
    employee = Contracts.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
