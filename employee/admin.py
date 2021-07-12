from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Employee
from .models import Team
from .models import JobName
from .models import Boss

@admin.register(Employee)
class ViewAdmim(ImportExportModelAdmin):
    pass

@admin.register(Team)
class ViewAdmim(ImportExportModelAdmin):
    pass

@admin.register(JobName)
class ViewAdmim(ImportExportModelAdmin):
    pass

@admin.register(Boss)
class ViewAdmim(ImportExportModelAdmin):
    pass