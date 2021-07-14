from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.apps import apps
from .models import Interview
from django.contrib import admin

# app = apps.get_app_config('interview')

# for model_name, model in app.models.items():
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

@admin.register(Interview)
class ViewAdmim(ImportExportModelAdmin):
    pass


