from django.shortcuts import render
from .forms import *
from .models import *


from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.forms.models import model_to_dict
from django.db.models import Sum, Count
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect



@login_required(login_url="/login/")
def appl_list(request):
    # if request.user.is_superuser:
    #     qs = Applicant.objects.all()
    # else:
    #     qs = Applicant.objects.filter(interviewer=request.user)
    context = {'appl_list': Applicant.objects.all()}
    return render(request, "applicant_list.html", context)


@login_required(login_url="/login/")
def appl_form(request):
    if request.POST and request.FILES['document']:
        form = ApplicantForm(request.POST, request.FILES or None)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return HttpResponse('Registro Completo')
        else:
            return render(request, "applicantForm.html", {'form': form})
    else:
        form = ApplicantForm()
    return render(request, 'applicantForm.html', {'form': form})




@login_required(login_url="/login/")
def test_list(request):
    # if request.user.is_superuser:
    #     qs = Applicant.objects.all()
    # else:
    #     qs = Applicant.objects.filter(interviewer=request.user)
    context = {'test_list': appTest.objects.all()}
    return render(request, "test_list.html", context)


def test_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = appTestForm()
        else:
            interview = appTest.objects.get(pk=id)
            employee_list = appTest.objects.all()
            form = appTestForm(instance=interview)
            contextabs = {'form': form, 'employee_list': employee_list}
        return render(request, "test_form.html", {'form': form, 'employee_list': appTest.objects.all()})
    else:
        if id == 0:
            form = appTestForm(request.POST)
        else:
            interview = appTest.objects.get(pk=id)
            
            form = appTestForm(request.POST,instance= interview)
        if form.is_valid():
            form.save()
            return HttpResponse('Hemos recibido sus respuestas, muchas gracias!')
        else:
            return render(request,"test_form.html",{'form':form})