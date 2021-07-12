from django.contrib import admin
from .models import Interview, Relation_e2e
from import_export.admin import ImportExportModelAdmin
from django.apps import apps
from django.apps import apps
from django.contrib import admin

# app = apps.get_app_config('interview')

# for model_name, model in app.models.items():
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# @admin.register(LeaveConcept)
# class ViewAdmim(ImportExportModelAdmin):
#     pass
admin.register(Relation_e2e)

@admin.register(Interview)
class ViewAdmim(ImportExportModelAdmin):
    pass
