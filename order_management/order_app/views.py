from django.shortcuts import render, redirect
from .models import *
from .forms import AddUserForm

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
    ordered = orders.filter(status='Zamówione').count()
    delivered = orders.filter(status='Dostarczone').count()

    context = {'orders': orders,
               'total_employees': total_employees,
               'total_orders': total_orders,
               'pending': pending,
               'ordered': ordered,
               'delivered': delivered,
               }
    template = 'order_app/index.html'

    return render(request, template, context)


def addUserView(request):
    if request.method != "POST":
        form = AddUserForm()
    else:
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('order_app:index')
    context = {'form': form}
    template = 'order_app/add_user.html'
    return render(request, template, context)






