from django.urls import path
from .views import *


app_name = 'order_app'

urlpatterns = [
    path('', indexView, name='index'),
    path('add_user/', addUserView, name='add_user'),

    path('orders/', ordersView, name='orders'),
    path('orders/<int:order_pk>/', orderView, name='order'),
    path('add_order/', addOrderView, name='add_order'),
    path('edit_orders/<int:order_pk>/', editOrderView, name='edit_order'),
    path('delete_order/<int:order_pk>/', deleteOrderView, name='delete_order'),

    path('orders/add_order_product/<int:order_pk>/', addOrderProductView, name='add_order_product'),
    path('orders/edit_order_product/<int:order_product_pk>/', editOrderProductView, name='edit_order_product'),
    path('orders/delete_order_product/<int:order_product_pk>/', deleteOrderProduct, name='delete_order_product'),

    path('users/', usersView, name='users'),
    path('add_user', addUserView, name='add_user'),
    path('edit_user/<int:employee_pk>/', editUserView, name='edit_user'),
]