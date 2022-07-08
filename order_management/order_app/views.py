from django.shortcuts import render
from .models import *

# Create your views here.
def indexView(request):
    # show amount of orders:
    orders = Order.objects.all()
    employees = Employee.objects.all()

    total_employees = employees.count()
    total_orders = orders.count()
    STATUS = (
        ('W trakcie zamówienia', 'W trakcie zamówienia'),
        ('Zamówiono', 'Zamówiono'),
        ('Dostarczono', 'Dostarczono'),
    )
    pending = orders.filter(status='W trakcie zamówienia').count()
    ordered = orders.filter(status='Zamówione')
    delivered = orders.filter(status='Dostarczone')

    context = {'orders': orders,
               'total_employees': total_employees,
               'total_orders': total_orders,
               'pending': pending,
               'ordered': ordered,
               'delivered': delivered,
               }
    template = 'order_app/index.html'

    return render(request, template, context)






