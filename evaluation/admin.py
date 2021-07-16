from django.contrib import admin
from .models import Test_Assign
from import_export.admin import ImportExportModelAdmin

#admin.site.register(Test_Assign)
@admin.register(Test_Assign)
class ViewAdmim(ImportExportModelAdmin):
    pass