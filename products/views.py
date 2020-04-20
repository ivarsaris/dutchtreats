from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReviewForm
from .models import Product, Review


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
    form = ReviewForm(request.POST)
    return render(request, "product.html", {'product': product, 'form': form})


def new_review(request, pk):
    """
    write a new review for a product on the single product page,
    or return error 404 if not found
    """
    if not request.user.is_authenticated:
        """redirect user to login page if not authenticated"""
        messages.warning(request, "You have to be logged in to post a review.")
        return redirect('login')

    else:
        """
        If user is logged in, allow them to write a review
        """
        reviews = Review.objects.all()
        product = get_object_or_404(Product, pk=pk)
        products = Product.objects.all()
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.post = product
                review.save()

                messages.success(
                    request, "Thanks for your review, it was saved successfully.")
                return redirect('product', pk=product.pk)

        form = ReviewForm()

    return render(request, 'product.html', {'form': form, 'products': products, 'reviews': reviews, 'product': product})


def delete_review(request, pk):
    """
    allow user to delete review
    """
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    messages.success(request, "You successfully deleted the review.")

    return render(request, 'index.html')
