from django.db import models
from django.conf import settings

from django.conf import settings

# Create your models here.
class AddInt(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    
    dated = models.DateTimeField(null=True, blank=True)
    interviewed = models.BooleanField()
    hire = models.BooleanField()
    interviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="interviewer"
    )

    def __str__(self):
        return self.hire