from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KQw1WKVc53T6uxDRI0F0lyLVBQSl4Iz4aea4eTbbp9WHJBKCewOmI9jEEkVx6wXI1smbiVIBGRVPHA6TzrEeH9Y00fN9p8rSH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
