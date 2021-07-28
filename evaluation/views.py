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
def test_assign_list(request):
    if request.user.is_superuser:
        qs = Test_Assign.objects.all()
    else:
        qs = Test_Assign.objects.filter(evaluator=request.user)
    context = {'test_assign_list': qs}
    return render(request, "test_list_2.html", context)


@login_required(login_url="/login/")
def rel_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Relation_Form()
        else:
            relation = Test_Assign.objects.get(pk=id)
          
            form = Relation_Form(instance=relation)
            
        return render(request, "relation_form.html", {'form': form, 'employee_list': Test_Assign.objects.all()})
    else:
        if id == 0:
            form = Relation_Form(request.POST)
            assessment = form.save(commit=False)
        else:
            relation = Test_Assign.objects.get(pk=id)
            form = Relation_Form(request.POST,instance= relation)
            assessment = form.save(commit=False)

        if form.is_valid():

            assessment.save()

            return redirect('/int_list')
        else:
            return render(request,"relation_form.html",{'form':form})
