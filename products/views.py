from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product

# Create your views here.
def all_products(request):
    """returns all products and renders them on products.html"""
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_detail(request, pk):
    """
    returns single product based on the ID(pk) and renders
    it on product.html. Or return error 404 if product not found
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {'product': product})
