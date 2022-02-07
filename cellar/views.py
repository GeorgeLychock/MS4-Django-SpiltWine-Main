from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import CellarItem
from products.models import Wine
from .forms import ItemForm


def view_cellar(request):
    """ View contents of the user's cellar """

    return render(request, 'cellar/cellar.html')


def add_to_cellar(request, item_id):
    """ Add a quantity of the specified product to the cellar db """

    wine = get_object_or_404(Wine, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
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

    quantity = int(request.POST.get('quantity'))
    user_id = 34
    cellar = CellarItem.objects.all()
    cellar = cellar.filter(cellar_user_pk=user_id)

    if quantity > 0:
        cellar[item_id] = quantity
    else:
        cellar.pop(item_id)

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