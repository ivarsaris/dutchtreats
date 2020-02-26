from django.shortcuts import render
from products.models import Product


"""allow user to search for a certain product in the products page"""
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
