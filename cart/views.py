from django.shortcuts import render


def view_cart(request):
    """ View to return index.html """

    return render(request, 'cart/cart.html')
