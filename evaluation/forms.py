from .models import Test_Assign
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Test_Assign
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args, **kwargs)
        pass