from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import User
from .models import Team
from .models import JobName



from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = ['username', 'identification']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('identification','mobile','doi','team','jobname','boss' )}),
    ) #this will allow to change these fields in admin module

admin.site.register(User, MyUserAdmin)

# @admin.register(User)
# class ViewAdmim(ImportExportModelAdmin):
#     pass

@admin.register(Team)
class ViewAdmim(ImportExportModelAdmin):
    pass

@admin.register(JobName)
class ViewAdmim(ImportExportModelAdmin):
    pass

