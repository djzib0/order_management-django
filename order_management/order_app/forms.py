from django import forms
from .models import Employee, OrderProduct

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


class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = '__all__'
        labels = {
            'product': 'Nazwa',
            'quantity': 'Ilość',
        }
        exclude = ['order']



