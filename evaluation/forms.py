from .models import Applicant, appTest
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('name','cc','document')
        labels = {
            'name': 'Nombre Completo',
            'cc':'No. Documento Identidad',
            'document': 'Evaluación'
        }
        
    def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cc'].widget.attrs.update({'class': 'form-control'})
        self.fields['document'].widget.attrs.update({'type': 'file'})

class appTestForm(forms.ModelForm):
    apprentice = forms.CharField(
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    identification = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={  
                "class": "form-control"
            }
        ))
    question1 = forms.CharField(
        widget=forms.Textarea(
            attrs={  
                "class": "form-control"
            }
        ))
    question4 = forms.CharField(
        widget=forms.Textarea(
            attrs={  
                "class": "form-control"
            }
        ))
    just5 = forms.CharField(
        widget=forms.Textarea(
            attrs={  
                "class": "form-control"
            }
        ))
    just6 = forms.CharField(
        widget=forms.Textarea(
            attrs={  
                "class": "form-control"
            }
        ))
    class Meta:
        model = appTest
        fields = ('apprentice','identification','question1','question2','question3','question4','question5','question6',)
        labels = {
            'apprentice': 'Aprendiz',
            'identification': 'No. de Identificacion',
            'question1': '¿Qué es la partida doble?',
            'question2': '¿Las máquinas son?',
            'question3': 'Un Anticipo a un Empleado, se ubica en',
            'question4': 'Explique la diferencia entre el capital de trabajo y el efectivo disponible.',
            'question5': 'Pregunta 5',
            'question6': 'Pregunta 6'
        }
    def __init__(self,*args, **kwargs):
        super(appTestForm, self).__init__(*args, **kwargs)
        self.fields['question2'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['question3'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['question5'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['question6'].widget.attrs.update({'class': 'form-dropdown'})
        #self.fields['question1'].widget.attrs.update({'class': 'form-control'})