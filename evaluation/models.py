from django.db import models
from django.utils import timezone
from django.conf import settings

class Test_Assign(models.Model):
    evaluated = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="employee_evaluated"
    )
    evaluator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="employee_evaluator"
    )
    relation = models.CharField(max_length=100,blank=True, null=True)
    done = models.CharField(max_length=100,blank=True, null=True,default="Asignado")

    def __str__(self):
        return self.evaluated.first_name + ' ' + self.evaluated.last_name 
