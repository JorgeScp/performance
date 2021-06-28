from django.db import models
from django.utils import timezone
from employee.models import Employee

class Contracts(models.Model):
    CONTRACTS = [
        ("FIJO 1 MES", 'FIJO 1 MES'),
        ('FIJO 3 MESES', 'FIJO 3 MESES'),
        ('FIJO 4 MESES', 'FIJO 4 MESES'),
        ('FIJO 6 MESES', 'FIJO 6 MESES'),
        ('FIJO 7 MESES', 'FIJO 7 MESES'),
    ]
    ENTERPRISES = [
        ("IMEXHS", 'IMEXHS'),
        ('RIMAB', 'RIMAB'),
        ('UT', 'UT'),
        ('COLSUBSIDIO', 'COLSUBSIDIO'),
    ]

    enterprise = models.CharField(
        max_length=30,
        choices=ENTERPRISES,
        default='RIMAB'
    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    t_contract = models.CharField(
        max_length=30,
        choices=CONTRACTS,
        default='FIJO 3 MESES'
    )
    idate_ctr = models.DateField()
    edate_ctr = models.DateField()
    not_date = models.DateField()
    notified = models.BooleanField()
    renew_ctr = models.BooleanField()
    observation = models.CharField(max_length=300,null=True)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.employee.fullname