from django.shortcuts import render, redirect
from django.db.models import Count, Sum, F
from .models import *
from .forms import AddUserForm, OrderProductForm, OrderForm, addOrderForm

# Create your views here.
def indexView(request):
    # show amount of orders:
    orders = Order.objects.all()
    employees = Employee.objects.all()

    total_employees = employees.count()
    total_orders = orders.count()
    STATUS = (
        ('W przygotowaniu', 'W przygotowaniu'),
        ('Zamówiono', 'Zamówiono'),
        ('Dostarczono', 'Dostarczono'),
    )
    pending = orders.filter(status='W przygotowaniu').count()
    ordered = orders.filter(status='Zamówiono').count()
    delivered = orders.filter(status='Dostarczono').count()

    context = {'orders': orders,
               'total_employees': total_employees,
               'total_orders': total_orders,
               'pending': pending,
               'ordered': ordered,
               'delivered': delivered,
               }
    template = 'order_app/index.html'

    return render(request, template, context)


def ordersView(request):
    orders = Order.objects.all().annotate(total_price=Sum(F('orderproduct__quantity')*F('product__price')))

    context = {'orders': orders,
               }
    template = 'order_app/orders.html'
    return render(request, template, context)

def orderView(request, order_pk):
    all_products = OrderProduct.objects.all().annotate(total_price=F('quantity')*F('product__price'))
    order_products = all_products.filter(order=Order.objects.get(id=order_pk)).order_by('product__name')
    order_total_value = order_products.aggregate(Sum('total_price'))

    # order_products = all_products.filter(order=Order.objects.get(id=order_pk)).values('product__name').annotate(total_quantity=Sum('quantity'))
    # order_products = order_products.values('product').annotate(total_quantity=Sum('quantity')).order_by('product')
    order = Order.objects.get(id=order_pk)
    context = {'order_products': order_products,
               'order': order,
               'order_pk': order_pk,
               'order_total_value': order_total_value,
               }
    template = 'order_app/order.html'
    return render(request, template, context)


def addOrderView(request):
    if request.method != 'POST':
        form = addOrderForm()
    else:
        form = addOrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('order_app:orders')

    context = {'form': form}
    template = 'order_app/add_order.html'
    return render(request, template, context)


def editOrderView(request, order_pk):
    order = Order.objects.get(id=order_pk)
    if request.method != 'POST':
        form = OrderForm(instance=order)
    else:
        form = OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_app:orders')

    context = {'form': form,
               'order': order,
               }
    template = 'order_app/edit_order.html'
    return render(request, template, context)


def deleteOrderView(request, order_pk):
    order = Order.objects.get(id=order_pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_app:orders')

    context = {}
    template = 'order_app/delete_order.html'

    return render(request, template, context)


def addOrderProductView(request, order_pk):
    order = Order.objects.get(id=order_pk)
    if request.method != "POST":
        form = OrderProductForm()
    else:
        form = OrderProductForm(request.POST)
        if form.is_valid():
            new_order_product = form.save(commit=False)
            new_order_product.order = order
            new_order_product.save()
            return redirect('order_app:order', order_pk=order.id)

    context = {
        'form': form,
        'order': order,
    }
    template = 'order_app/add_order_product.html'
    return render(request, template, context)


def editOrderProductView(request, order_product_pk):
    order_product = OrderProduct.objects.get(id=order_product_pk)
    order = Order.objects.get(id=order_product.order.id)
    if request.method != 'POST':
        form = OrderProductForm(instance=order_product)
    else:
        form = OrderProductForm(instance=order_product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_app:order', order_pk=order_product.order.id)

    context = {'order_product': order_product,
               'form': form,
               'order': order,
               }
    template = 'order_app/edit_order_product.html'
    return render(request, template, context)


def deleteOrderProduct(request, order_product_pk):
    order_product = OrderProduct.objects.get(id=order_product_pk)
    go_back_id = order_product.order.id
    if request.method == 'POST':
        order_product.delete()
        return redirect('order_app:order', order_pk=go_back_id)

    context = {'order_product': order_product,
               'go_back_id': go_back_id}
    template = 'order_app/delete_order_product.html'
    return render(request, template, context)


def usersView(request):
    users = Employee.objects.all()

    context = {'users': users}
    template = 'order_app/users.html'

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


def editUserView(request, employee_pk):
    employee = Employee.objects.get(id=employee_pk)
    if request.method != 'POST':
        form = AddUserForm(instance=employee)
    else:
        form = AddUserForm(instance=employee, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('order_app:users')

    context = {'employee': employee,
               'form': form,
               }
    template = 'order_app/edit_user.html'
    return render(request, template, context)










