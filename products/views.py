from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def single_product(request):
    product = Product.object()
    return render(request, "single_product.html", {'product': product})
