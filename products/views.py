from django.shortcuts import render, get_object_or_404
from .models import Wine


def all_products(request):
    """ Shows all products and handles sorting and searching. """

    wines = Wine.objects.all()

    wine_content = {
        'wines': wines,
    }

    return render(request, 'products/products.html', wine_content)


def all_wines(request):
    """ Shows all products and handles sorting and searching. """

    wines = Wine.objects.all()

    wine_content = {
        'wines': wines,
    }

    return render(request, 'products/wines.html', wine_content)

def wine_detail(request, product_id):
    """ Shows the wine product details. """

    wine = get_object_or_404(Wine, pk=product_id)

    wine_content = {
        'wine': wine,
    }

    return render(request, 'products/wine_detail.html', wine_content)
