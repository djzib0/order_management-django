from django.urls import path
from .views import *


app_name = 'order_app'

urlpatterns = [
    path('', indexView, name='index')
]