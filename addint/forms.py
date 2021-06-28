from .models import AddInt
from django import forms

class AddIntForm(forms.ModelForm):
    class Meta:
        model = AddInt
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddIntForm, self).__init__(*args, **kwargs)
        self.fields['dated'].widget.attrs.update({'class': 'form-control','id':'datepicker4'})
        self.fields['dated'].input_formats=['%Y-%m-%d %H:%M:%S']
        self.fields['employee'].empty_label = "Select"
        self.fields['employee'].widget.attrs.update({'class': 'form-dropdown', 'id':'selectemp4'})