from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
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
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    @property
    def multiply_price_quantity(self):
        return 2

class Order(models.Model):
    STATUS = (
        ('W przygotowaniu', 'W przygotowaniu'),
        ('Zamówiono', 'Zamówiono'),
        ('Dostarczono', 'Dostarczono'),
    )
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ManyToManyField(Product, through="OrderProduct")
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    note = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"




class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Zamówienie {self.order.id}"

