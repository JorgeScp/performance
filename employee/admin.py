from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import Team
from .models import JobName
from .models import Boss

admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(JobName)
admin.site.register(Boss)