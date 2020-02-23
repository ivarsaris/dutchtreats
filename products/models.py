from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    """Product models, add product to the database"""
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Review(models.Model):
    """model to write review for a product"""
    post = models.ForeignKey(Product, related_name='reviews')
    user = models.ForeignKey(User, related_name='reviews', null=False, default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200, default='my review')
    content = models.TextField()
    review_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.content
