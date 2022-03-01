from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Wine, Varietal, CountryState
from .forms import ProductForm


def all_products(request):
    # """ Shows products and handles sorting and searching. """

    # Add queries to fetch all categories of product data
    products = Wine.objects.all()
    query = None
    query_term = None
    featured = []

    # wine_accessories = WineAccessories.objects.all()
    # culinary = Culinary.objects.all()

    # combine queries
    # products = .JOIN()

    # Execute Search query
    if request.GET:
        if 'q1' in request.GET:
            query = request.GET['q1']
            if not query:
                messages.error(request, "Please enter some search criteria.")
                return redirect('home')

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            featured = products.filter(featured=True)
            # if featured.length() == 0:
            #     featured = []
            query_term = str.title(query)
    

    all_content = {
        'products': products,
        'search_term': query_term,
        'featured': featured,
    }

    return render(request, 'products/products.html', all_content)


def all_wines(request):
    """ Shows all products and handles sorting and searching. """

    # wines = Wine.objects.filter(country_state=1)
    # sort_target ="California"
    wines = Wine.objects.all()
    varietals = None
    sort = 'All Wines'
    direction = None
    countries = None
    country = None
    featured = wines.filter(featured=True)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # if sorting by name, direction. From Code Institute, https://codeinstitute.net/global/
            if sortkey == 'name':
                sortkey = 'lower_name'
                wines = wines.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            wines = wines.order_by(sortkey)
        
        if 'country_state' in request.GET:
            countries = CountryState.objects.all()
            country = request.GET['country_state']
            # all wines, sorted by alpha country/state
            if not country:
                sort = "Country / State"
                sortkey = 'country_state__name'
            # wines sorted by specific country/state
            if country:
                wines = wines.filter(country_state__name=country)
                featured = featured.filter(country_state__name=country)
                sortkey = 'name'
                sort = country
                
            wines = wines.order_by(sortkey)

        if 'varietal' in request.GET:
            varietal = request.GET['varietal']
            # wines sorted by specific varietal
            if varietal:
                varietals = Varietal.objects.all()
                wines = wines.filter(varietal__name=varietal)
                sortkey = 'name'
                sort = varietal
                
            wines = wines.order_by(sortkey)
    
    current_sorting = f'{sort}_{direction}'
    sorting = str.title(sort)

    wine_content = {
        'wines': wines,
        'current_sorting': current_sorting,
        'sorting': sorting,
        'countries': countries,
        'featured': featured,
        'varietals': varietals,
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

@login_required
def add_wine(request):
    """ Add a wine to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added your wine!')
            return redirect('wine_detail', product.pk)
        else:
            messages.error(request, 'Failed to add your wine. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_wine.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_wine(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    product = get_object_or_404(Wine, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect('wine_detail', product.pk)
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_wine.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_wine(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    product = get_object_or_404(Wine, pk=product_id)
    product.delete()
    messages.success(request, 'Wine deleted!')
    return redirect('wines')