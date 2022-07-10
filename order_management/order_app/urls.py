from django.urls import path
from .views import *


app_name = 'order_app'

urlpatterns = [
    path('', indexView, name='index'),
    path('add_user/', addUserView, name='add_user'),
    path('orders/', ordersView, name='orders'),
    path('orders/<int:order_pk>/', orderProductView, name='order'),
]