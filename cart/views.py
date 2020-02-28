from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

def view_cart(request):
    """render the cart contents page"""
    return render(request, 'cart.html')

"""add specific amount of a product to the cart"""
def add_to_cart(request, id):
    if not request.user.is_authenticated:

        """redirect user to login page if not authenticated"""
        messages.warning(request, "You have to be logged in to add products to your cart.")
        return redirect('login')
    
    else:
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})
        cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        return redirect(reverse('products'))


def adjust_cart(request, id):
    """adjust amount of product in the cart by specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
