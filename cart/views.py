from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse


def view_cart(request):
    """render the cart contents page. if user is not logged in, they're redirected 
    to login page with message. Else, they're cart is opened"""
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO,
                             'You must be logged in to visit your cart.')
        return redirect('login')
    else:
        return render(request, 'cart.html')

"""add specific amount of a product to the cart"""
def add_to_cart(request, id):
    if not request.user.is_authenticated:

        """redirect user to login page if not authenticated"""
        messages.warning(request, "You have to be logged in to add products to your cart.")
        return redirect(reverse('login'))
    
    else:
        quantity = int(request.POST.get('quantity'))

        if not quantity:
            messages.warning(request, "Please select an amount.")
            return redirect('login')

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
