from django.db import models
from products.models import Product


"""get all neccessary information for order to be placed"""
class Order(models.Model):
    full_name = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    postal_code = models.CharField(max_length=15, blank=False)
    province = models.CharField(max_length=25, blank=False)
    country = models.CharField(max_length=25, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
