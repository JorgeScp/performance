from .models import Test_Assign
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class Relation_Form(forms.ModelForm):
    class Meta:
        model = Test_Assign
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(Relation_Form, self).__init__(*args, **kwargs)
        self.fields['evaluator'].empty_label = "Select"
        self.fields['evaluator'].widget.attrs.update({'class': 'form-dropdown', 'id':'selectevaluated'})
        self.fields['evaluated'].empty_label = "Select"
        self.fields['evaluated'].widget.attrs.update({'class': 'form-dropdown', 'id':'selectevaluator'})
        self.fields['relation'].widget.attrs.update({'class': 'form-control'})
        self.fields['done'].widget.attrs.update({'class': 'form-control'})
