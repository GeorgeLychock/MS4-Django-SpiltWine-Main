from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from products.models import Wine


def view_cart(request):
    """ View contents of the user's cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    """ from Code Institute, Django Module
     https://codeinstitute.net/global/ """

    product = get_object_or_404(Wine, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request,
                         f'Cart Updated! {product.name}Quantity changed to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request,
                         f'Added {product.name} to your cart! Click the cart icon to view.')
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update the cart item parameters """
    """ from Code Institute, Django Module """
    """ https://codeinstitute.net/global/ """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, item_id):
    """ Remove item from cart """
    """ from Code Institute, Django Module """
    """ https://codeinstitute.net/global/ """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
            return HttpResponse(status=500)
