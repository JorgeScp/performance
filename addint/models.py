from django.db import models
from employee.models import Employee
from django.contrib.auth.models import User

# Create your models here.
class AddInt(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    dated = models.DateTimeField(null=True, blank=True)
    interviewed = models.BooleanField()
    hire = models.BooleanField()
    interviewer = models.ForeignKey(User,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.employee.fullname