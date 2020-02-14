from django.shortcuts import render, reverse, redirect

# Create your views here.
def view_cart(request):
    """render the cart contents page"""
    return render(request, 'cart.html')

def add_to_cart(request, id):
    """add specific amount of a product to the cart"""
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
