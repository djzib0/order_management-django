from django import forms
from .models import Employee, OrderProduct, Order

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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {'employee': 'Pracownik',
                  'status': 'Status',
                  'note': 'Uwagi',
                  }
        exclude = ['date_created', 'product']


class addOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {'employee': 'Pracownik',
                  'status': 'Status',
                  'note': 'Uwagi',
                  }
        exclude = ['product']





