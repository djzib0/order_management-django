from django.shortcuts import render
from .models import *

# Create your views here.
def indexView(request):
    context = {}
    return render(request, 'order_app/index.html', context)

