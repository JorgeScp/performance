from .models import Interview
from django import forms
from django.core.validators import RegexValidator

class InterviewForm(forms.ModelForm):
    strengths = forms.CharField(
        label="Fortalezas",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
    ))
    oportunities_areas = forms.CharField(
        label="Áreas de Oportunidad",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
    ))
    general_question = forms.CharField(
        label="¿Qué le sugerirías al evaluado para mejorar su desempeño profesional y personal?",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
    ))
    observations = forms.CharField(
        label="Observaciones",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
    ))
    class Meta:
        model = Interview
        fields = '__all__'
        exclude = ('result','touser')
        labels = {
            'evaluator':'Evaluador',
            'evaluated':'Evaluado',
            'dated':'Fecha Evaluación',
            #Labels for questions======================
            'comunicacion_1':'La información que comparte es clara y asertiva.',
            'comunicacion_2':'Es receptivo a las opiniones y sugerencias de los demás.',
            'comunicacion_3':'Escucha y presta atención a las conversaciones.',
            'comunicacion_4':'Su comunicación escrita es clara, concisa y efectiva.',
            'comunicacion_5':'Expresa sus ideas con claridad y respeto a los demás.',
            'trabajo_equipo_1':'Se desempeña como un miembro activo del equipo.',
            'trabajo_equipo_2':'Motiva y guía al equipo para el logro de los objetivos establecidos.',
            'trabajo_equipo_3':'Fomenta el diálogo de manera abierta y directa. ',
            'servicio_cliente_1':'Es cortes y amable en el trato que tiene con el cliente',
            'servicio_cliente_2':'Se gestionan correctamente las solicitudes para dar respuesta de manera oportuna.',
            'servicio_cliente_3':'Realiza de manera oportuna, feedback a los procesos',
            'resolucion_problemas_1':'Busca la información suficiente para la toma de decisiones.',
            'resolucion_problemas_2':'Es flexible al cambio en las diferentes situaciones que se presentan. ',
            'resolucion_problemas_3':'Considera las implicaciones antes de llevar a cabo una acción. ',
            'resolucion_problemas_4':'Conserva la calma en situaciones complicadas. ',
            'resolucion_problemas_5':'Es propositivo en las diferentes situaciones que requieran soluciones o toma de decisiones de impacto. ',
            'liderazgo_1':'Se adapta a trabajar con nuevos procesos y tareas. ',
            'liderazgo_2':'No muestra resistencia a las ideas de las demás personas.',
            'liderazgo_3':'Comparte su conocimiento, habilidades y experiencia.',
            'liderazgo_4':'Comparte el reconocimiento de logros con el resto del equipo.',
            'liderazgo_5':'Busca reforzar sus habilidades y trabajar en sus áreas de oportunidad',
            'admon_tiempo_1':'Establece prioridades en sus actividades laborales cumpliento con las metas y objetivos establecidos.',
            'admon_tiempo_2':'Cumple con los tiempo y forma los proyectos asignados',
            'admon_tiempo_3':'Utiliza eficientemente los recursos asignados para llevar a cabo sus actividades. ',
            'pensamiento_estrategico_1':'Comprende las implicaciones de sus decisiones en el negocio a corto y largo plazo.',
            'pensamiento_estrategico_2':'Determina objetivos y establece prioridades para lograrlos.',
            'pensamiento_estrategico_3':'Tiene visión a largo plazo y busca oportunidades paracumplir con las metas de organización desde su área.',
            'pensamiento_estrategico_4':'Es percibido por el cliente como una persona confiable que representa a la empresa. ',
            'enfoque_resultados_1':'Reconoce y aprovecha las oportunidades que se presentan en las diferentes situaciones.',
            'enfoque_resultados_2':'Mantiene altos niveles de estándares de desempeño ',
            'enfoque_resultados_3':'Sus resultados son sobresalientes y generan valor a la empresa. ',
            'enfoque_resultados_4':'Es detallista con la información que presenta y en pocas ocasiones se detectan inconsistencias o errores. ',
            
            
            #__________________________________________
        }

    def __init__(self, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)
        #self.fields['days'].validators = [RegexValidator(r'^[\d]{1,3}$', message="Value must be an integer and less than 3 numbers long")]
        # self.fields['leaveconcept'].empty_label = "Select"
        # self.fields['leaveconcept'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['dated'].widget.attrs.update({'class': 'form-control','id':'datepicker'})
        self.fields['dated'].input_formats=['%Y-%m-%d %H:%M:%S']
        self.fields['evaluator'].empty_label = "Select"
        self.fields['evaluator'].widget.attrs.update({'class': 'form-dropdown', 'id':'selectemp'})
        self.fields['evaluated'].empty_label = "Select"
        self.fields['evaluated'].widget.attrs.update({'class': 'form-dropdown', 'id':'selecte2'})
        
        #Make form control all questions
        self.fields['comunicacion_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunicacion_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunicacion_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunicacion_4'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunicacion_5'].widget.attrs.update({'class': 'form-control'})
        self.fields['trabajo_equipo_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['trabajo_equipo_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['trabajo_equipo_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['servicio_cliente_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['servicio_cliente_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['servicio_cliente_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['resolucion_problemas_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['resolucion_problemas_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['resolucion_problemas_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['resolucion_problemas_4'].widget.attrs.update({'class': 'form-control'})
        self.fields['resolucion_problemas_5'].widget.attrs.update({'class': 'form-control'})
        self.fields['liderazgo_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['liderazgo_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['liderazgo_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['liderazgo_4'].widget.attrs.update({'class': 'form-control'})
        self.fields['liderazgo_5'].widget.attrs.update({'class': 'form-control'})
        self.fields['admon_tiempo_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['admon_tiempo_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['admon_tiempo_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['pensamiento_estrategico_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['pensamiento_estrategico_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['pensamiento_estrategico_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['pensamiento_estrategico_4'].widget.attrs.update({'class': 'form-control'})
        self.fields['enfoque_resultados_1'].widget.attrs.update({'class': 'form-control'})
        self.fields['enfoque_resultados_2'].widget.attrs.update({'class': 'form-control'})
        self.fields['enfoque_resultados_3'].widget.attrs.update({'class': 'form-control'})
        self.fields['enfoque_resultados_4'].widget.attrs.update({'class': 'form-control'})
       


        #elf.fields['touser'].disabled = True

