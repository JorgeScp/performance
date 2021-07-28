from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.hashers import make_password
from import_export import resources, fields

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
            (None, {'fields': ('identification','mobile','doi','team','jobname','boss_name','boss_job_name' )}),
    ) #this will allow to change these fields in admin module

#admin.site.register(User, MyUserAdmin)

class UserResource(resources.ModelResource):
    def before_import_row(self,row, **kwargs):
        value = row['password']
        row['password'] = make_password(value)
    class Meta:
        model = User

@admin.register(User)
class ViewAdmim(ImportExportModelAdmin):
    resource_class = UserResource

#admin.site.register(MyUserAdmin)
# class ViewAdmim(ImportExportModelAdmin):
#     pass

@admin.register(Team)
class ViewAdmim(ImportExportModelAdmin):
    pass

@admin.register(JobName)
class ViewAdmim(ImportExportModelAdmin):
    pass

