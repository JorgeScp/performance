from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    identification = forms.CharField(
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname':'Full Name',
            'identification':'identification'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['jobname'].empty_label = "Select"
        self.fields['jobname'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['team'].empty_label = "Select"
        self.fields['team'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['identification'].required = False
        self.fields['doi'].widget.attrs.update({'class': 'form-control','id':'datepicker'})
        self.fields['doi'].input_formats=['%Y-%m-%d %H:%M:%S']

