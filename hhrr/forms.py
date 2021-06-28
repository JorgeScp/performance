from .models import Contracts
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class ContractsForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'
        # labels = {
        #     'apprentice': 'Aprendiz',
        #     'identification': 'No. de Identificacion',
        #     'question1': '¿Qué es la partida doble?',
        #     'question2': '¿Las máquinas son?',
        #     'question3': 'Un Anticipo a un Empleado, se ubica en',
        #     'question4': 'Explique la diferencia entre el capital de trabajo y el efectivo disponible.',
        #     'question5': 'Pregunta 5',
        #     'question6': 'Pregunta 6'
        # }
    def __init__(self,*args, **kwargs):
        super(ContractsForm, self).__init__(*args, **kwargs)
        self.fields['idate_ctr'].widget.attrs.update({'class': 'form-control','id':'datepicker'})
        self.fields['idate_ctr'].input_formats=['%Y-%m-%d %H:%M:%S']
        self.fields['edate_ctr'].widget.attrs.update({'class': 'form-control','id':'datepicker1'})
        self.fields['edate_ctr'].input_formats=['%Y-%m-%d %H:%M:%S']
        self.fields['not_date'].widget.attrs.update({'class': 'form-control','id':'datepicker2'})
        self.fields['not_date'].input_formats=['%Y-%m-%d %H:%M:%S']
        self.fields['t_contract'].empty_label = "Select"
        self.fields['t_contract'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['enterprise'].empty_label = "Select"
        self.fields['enterprise'].widget.attrs.update({'class': 'form-dropdown'})