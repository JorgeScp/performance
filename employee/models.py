from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50, default="none")
    def __str__(self):
        return self.name


class JobName(models.Model):
    name = models.CharField(max_length=50,default="none")

    def __str__(self):
        return self.name

class User(AbstractUser):
    
    identification = models.IntegerField(null=True,blank=True)
    mobile= models.IntegerField(null=True,blank=True)
    
    doi = models.DateField(null=True, blank=True)
    team = models.CharField(max_length=300,null=True,blank=True,default="NA")
    jobname = models.CharField(max_length=300,null=True,blank=True,default="NA")
    boss = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="Boss"
    )
    
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + ' ' + self.last_name
