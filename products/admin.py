from django.contrib import admin
from .models import Product, Review

"""registering product and review to the admin panel"""
admin.site.register(Product)
admin.site.register(Review)