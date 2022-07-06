from django.contrib import admin
from .models import Employee, Product, Order

# Register your models here.
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Order)
