from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from .models import LeaveConcept, Absenteeism
from import_export.admin import ImportExportModelAdmin
from django.apps import apps
from django.apps import apps
from django.contrib import admin

app = apps.get_app_config('addint')

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass