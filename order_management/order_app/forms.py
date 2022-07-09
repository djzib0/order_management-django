from django import forms
from .models import Employee

class AddUserForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'name': 'Imię',
            'surname': 'Nazwisko',
            'phone': 'Nr telefonu',
            'email': 'E-mail',
        }



