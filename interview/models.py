from django.db import models
from django.db.models.aggregates import Max
from django.conf import settings
from django.contrib.auth.models import User
MIN = 0
MAX = 100
from django.core.validators import MinValueValidator, MaxValueValidator


class Interview(models.Model):
    dated = models.DateField(null=True, blank=True)
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True, related_name='evaluator')
    evaluated = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True, related_name='evaluated')
    relation = models.CharField(null=True, blank=True,max_length=200,default="No Asignado")
    #=========================================================================================
    # QUESTIONS MODELS
    #=========================================================================================
    #__________________1
    comunicacion_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    comunicacion_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    comunicacion_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    comunicacion_4 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    comunicacion_5 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)

    comunicacion_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    #__________________2
    trabajo_equipo_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    trabajo_equipo_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    trabajo_equipo_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)

    trabajo_equipo_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    #__________________3
    servicio_cliente_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    servicio_cliente_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    servicio_cliente_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)

    servicio_cliente_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    #__________________4
    resolucion_problemas_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    resolucion_problemas_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    resolucion_problemas_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    resolucion_problemas_4 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    resolucion_problemas_5 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)

    resolucion_problemas_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    #__________________5
    liderazgo_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    liderazgo_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    liderazgo_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    liderazgo_4 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    liderazgo_5 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)

    liderazgo_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    #__________________6
    admon_tiempo_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    admon_tiempo_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    admon_tiempo_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)

    admon_tiempo_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    #__________________7
    pensamiento_estrategico_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)	 
    pensamiento_estrategico_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)	 
    pensamiento_estrategico_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)	 
    pensamiento_estrategico_4 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)	 

    pensamiento_estrategico_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)	 
    #__________________8
    enfoque_resultados_1 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    enfoque_resultados_2 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    enfoque_resultados_3 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    enfoque_resultados_4 = models.IntegerField(validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    
    enfoque_resultados_r = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(MIN), MaxValueValidator(MAX)],default=100)
    #=========================================================================================
    result = models.CharField(null=True, blank=True,max_length=50,default="0")
    #=========================================================================================
    strengths = models.CharField(null=True, blank=True,max_length=200,default="0")
    oportunities_areas = models.CharField(null=True, blank=True,max_length=200,default="0")
    general_question = models.CharField(null=True, blank=True,max_length=200,default="0")
    observations = models.CharField(null=True, blank=True,max_length=200,default="Ninguna")


    #visa = models.BooleanField(default=False)
    #no_children = models.IntegerField(null=True, blank=True)