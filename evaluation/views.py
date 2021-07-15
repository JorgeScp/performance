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


