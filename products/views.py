from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Wine, Varietal


def all_products(request):
    # """ Shows products and handles sorting and searching. """

    # Add queries to fetch all categories of product data
    products = Wine.objects.all()
    query = None

    # wine_accessories = WineAccessories.objects.all()
    # culinary = Culinary.objects.all()

    # combine queries
    # products = .JOIN()

    if request.GET:
        if 'q1' in request.GET:
            query = request.GET['q1']
            if not query:
                messages.error(request, "Please enter some search criteria.")
                return redirect('home')

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    all_content = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', all_content)


def all_wines(request):
    """ Shows all products and handles sorting and searching. """

    wines = Wine.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                wines = wines.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            wines = wines.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    wine_content = {
        'wines': wines,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/wines.html', wine_content)


def wine_detail(request, product_id):
    """ Shows the wine product details. """

    wine = get_object_or_404(Wine, pk=product_id)

    wine_content = {
        'wine': wine,
    }

    return render(request, 'products/wine_detail.html', wine_content)


def varietals(request):
    """ Shows the wine varietal view """

    varietals = Varietal.objects.all()

    varietal_content = {
        'varietals': varietals,
    }

    return render(request, 'products/varietals.html', varietal_content)