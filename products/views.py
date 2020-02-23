from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages


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
        # redirect user to login page if not authenticated
        messages.warning(request, "You have to be logged in to post a review.")
        return redirect('login')

    else:
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

                messages.success(request, "Thanks for your review, it was saved successfully.")
                return redirect('product', pk=product.pk)
            
        form = ReviewForm()
    
    return render(request, 'product.html', {'form': form, 'products': products, 'reviews': reviews, 'product': product})


def edit_review(request, pk):
    """allow user to edit review"""
    reviews = Review.objects.all()
    products = Product.objects.all()
    review = get_object_or_404(Review, pk=pk)
    # allow user to edit review if they are the review owner or admin
    if (request.user.is_authenticated and request.user == review.owner or request.user.is_superuser):
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                review = form.save()
                return redirect('product', review.post.id)
        else:
            form = ReviewForm(instance=review)
    else:
        return HttpResponseForbidden()

    return render(request, 'product.html', {'form': form, 'products': products, 'reviews': reviews, 'post': review.post})


def delete_review(request, pk):
    """allow user to delete review"""
    # id = request.POST['review_id']  - From form related code.
    # pk = request.POST['product_id'] - From form related code.
    product = get_object_or_404(Product, pk=pk)
    review = get_object_or_404(Review, pk=pk)
    if (request.user.is_authenticated and request.user == review.user or request.user.is_superuser):
        if request.method == 'POST':
            try:
                review.delete()
                messages.success(request, "You successfully deleted the review.")

            except review.DoesNotExist:
                messages.warning(request, "You can't delete this comment.")

    else:
        print("failed on checking user")
        return HttpResponseForbidden()

    return render(request, 'index.html')
