from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
import datetime


# Create your models here.

CATEGORY_CHOICES = (
    ('Shirt', 'Shirt'),
    ('Sport wear', 'Sport wear'),
    ('Jeans', 'Jeans')
)


# SEX_CHOICES = (
#     ('Male', 'Male'),
#     ('Female', 'Female'),
#     ('Others', 'Others')
# )

class Vendor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    description = models.TextField()
    price = MoneyField(max_digits=19, decimal_places=2, default_currency='USD')
    image = models.ImageField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=40)
    phone_number = PhoneNumberField()
    # sex = models.CharField(choices=SEX_CHOICES, max_length=15)


    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=40, blank=True, null=True)
    order_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.customer.name