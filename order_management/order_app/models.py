from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"


class Product(models.Model):
    CATEGORY = (
        ('Artykuły papiernicze', 'Artykuły papiernicze'),
        ('Zabawki', 'Zabawki')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, choices=CATEGORY, null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.name}"



class Order(models.Model):
    STATUS = (
        ('W trakcie zamówienia', 'W trakcie zamówienia'),
        ('Zamówiono', 'Zamówiono'),
        ('Dostarczono', 'Dostarczono'),
    )
    user = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f"{self.product}"
