from django.db import models
from django.utils import timezone
from employee.models import Employee

class Applicant(models.Model):
    name = models.CharField(max_length=100,null=True)
    cc = models.IntegerField(null=True)
    document = models.FileField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

class appTest(models.Model):
    Activos_circulantes = 'AC'
    Activos_fijos = 'AF'
    Pasivos_fijos = 'PF'
    Pasivos_Circulantes = 'PC'
    MAQUINA = [
        (Activos_circulantes, 'Activos circulantes'),
        (Activos_fijos, 'Activos fijos'),
        (Pasivos_fijos, 'Pasivos fijos'),
        (Pasivos_Circulantes, 'Pasivos Circulantes'),
    ]

    Pasivo_corriente = 'PC'
    activo_exigible = 'AE'
    activo_realizable = 'AR'
    activo_diferido = 'AD'
    ANTICIPO = [
        (Pasivo_corriente, 'Pasivo corriente'),
        (activo_exigible, 'activo exigible'),
        (activo_realizable, 'activo realizable'),
        (activo_diferido, 'activo diferido'),
    ]

    img1 = 'PC'
    img2 = 'AE'
    img3 = 'AR'
    img4 = 'AD'
    IMAGEN1 = [
        (img1, 'Imagen 1'),
        (img2, 'Imagen 2'),
        (img3, 'Imagen 3'),
        (img4, 'Ninguna de las anteriores'),
    ]

    img11 = 'PC'
    img22 = 'AE'
    img33 = 'AR'
    img44 = 'AD'
    IMAGEN2 = [
        (img11, 'Imagen 1'),
        (img22, 'Imagen 2'),
        (img33, 'Imagen 3'),
        (img44, 'Ninguna de las anteriores'),
    ]

    apprentice = models.CharField(max_length=100,blank=True, null=True)
    identification = models.IntegerField(null=True)
    question1 = models.CharField(max_length=1000,blank=True, null=True)
    question2 = models.CharField(
        max_length=2,
        choices=MAQUINA,
        default=Activos_circulantes,
    )
    question3 = models.CharField(
        max_length=2,
        choices=ANTICIPO,
        default=Activos_circulantes,
    )
    question4 = models.CharField(max_length=1000,blank=True, null=True)
    question5 = models.CharField(
        max_length=2,
        choices=IMAGEN1,
        default=Activos_circulantes,
    )
    just5 = models.CharField(max_length=1000,blank=True, null=True)
    question6 = models.CharField(
        max_length=2,
        choices=IMAGEN2,
        default=Activos_circulantes,
    )
    just6 = models.CharField(max_length=1000,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.apprentice