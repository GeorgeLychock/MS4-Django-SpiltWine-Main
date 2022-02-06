from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import CellarItem
from products.models import Wine
from .forms import ItemForm


def view_cellar(request):
    """ View contents of the user's cellar """

    return render(request, 'cellar/cellar.html')


def add_to_local_cellar(request, item_id):
    """ Add a quantity of the specified product to the cellar db """

    quantity = int(request.POST.get('local_cellar_quantity'))
    redirect_url = request.POST.get('redirect_url')
    cellar = request.session.get('cellar', {})

    if item_id in list(cellar.keys()):
        cellar[item_id] += quantity
    else:
        cellar[item_id] = quantity

    request.session['cellar'] = cellar
    return redirect(redirect_url)


def add_to_cellar(request, item_id):
    """ Add a quantity of the specified product to the cellar db """
    wine = get_object_or_404(Wine, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # form.fields['cellar_wine_name'] = item_id
            form.save()
            return redirect('cellar')
    form = ItemForm()
    context = {
        'form': form,
        'wine': wine,
    }
    return render(request, 'cellar/add_to_cellar.html', context)


def update_cellar(request, item_id):
    """ Update the cellar item parameters """
    """ from Code Institute, Django Module https://codeinstitute.net/global/ """

    quantity = int(request.POST.get('quantity'))
    cellar = request.session.get('cellar', {})

    if quantity > 0:
        cellar[item_id] = quantity
    else:
        cellar.pop(item_id)

    request.session['cellar'] = cellar
    return redirect('cellar')


def remove_from_cellar(request, item_id):
    """ Remove item from cellar """
    """ from Code Institute, Django Module https://codeinstitute.net/global/ """
    try:
        cellar = request.session.get('cellar', {})
        cellar.pop(item_id)

        request.session['cellar'] = cellar
        return HttpResponse(status=200)
    except Exception as e:
            return HttpResponse(status=500)