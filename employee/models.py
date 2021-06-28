from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50, default="none")
    def __str__(self):
        return self.name

class Boss(models.Model):
    name = models.CharField(max_length=50, default="none")

    def __str__(self):
        return self.name

class JobName(models.Model):
    name = models.CharField(max_length=50,default="none")

    def __str__(self):
        return self.name

class Employee(models.Model):
    fullname = models.CharField(max_length=100, default="none")
    identification = models.IntegerField(null=True,blank=True)
    mobile= models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    doi = models.DateTimeField(null=True, blank=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,default=1)
    jobname = models.ForeignKey(JobName,on_delete=models.CASCADE,default=1)
    boss = models.ForeignKey(Boss,on_delete=models.CASCADE,default=1)
    

    def __str__(self):
        return self.fullname
