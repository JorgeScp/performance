from django.shortcuts import render
from .models import *
from .forms import *
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from employee.models import Employee
from django.forms.models import model_to_dict
from django.db.models import Sum, Count

@login_required(login_url="/login/")
def addint_list(request):
    if request.user.is_superuser:
        qs = AddInt.objects.all()
    else:
        qs = AddInt.objects.filter(interviewer=request.user)
    context = {'addint_list': qs}
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def item_update(request, id=0):
    addint_list = AddInt.objects.get(pk=id)
    addint_list.interviewed ^= True
    addint_list.save()
    return redirect('/')

@login_required(login_url="/login/")
def item_update_concept(request, id=0):
    item = AddInt.objects.get(pk=id)
    item.hire ^= True
    item.save()
    return redirect('/') 

@login_required(login_url="/login/")
def addint_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AddIntForm()
        else:
            addint = AddInt.objects.get(pk=id)
            employee_list = Employee.objects.all()
            form = AddIntForm(instance=addint)
            contextabs = {'form': form, 'employee_list': employee_list}
        return render(request, "addint_form.html", {'form': form, 'employee_list': Employee.objects.all()})
    else:
        if id == 0:
            form = AddIntForm(request.POST)
        else:
            addint = AddInt.objects.get(pk=id)
            
            form = AddIntForm(request.POST,instance= addint)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,"addint_form.html",{'form':form})

@login_required(login_url="/login/")
def addint_delete(request,id):
    addint = AddInt.objects.get(pk=id)
    addint.delete()
    return redirect('/')