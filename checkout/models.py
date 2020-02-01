from django.db import models
from products.models import Product

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    postal_code = models.CharField(max_length=15, blank=False)
    province = models.CharField(max_length=25, blank=False)
    country = models.CharField(max_length=25, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2} {3}".format(self.id, self.date, self.first_name, self.last_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} * {1} for €{2}".format(self.quantity, self.product.name, self.product.price)
