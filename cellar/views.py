from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CellarItem
from products.models import Wine
from .forms import ItemForm


@login_required
def view_cellar(request):
    """ View contents of the user's cellar """

    return render(request, 'cellar/cellar.html')


@login_required
def add_to_cellar(request, item_id):
    """ Add a wine to user's cellar, if one already exists, redirect to update """
    
    form = ItemForm()
    wine = get_object_or_404(Wine, pk=item_id)
    user_id = request.user.pk

    # Check if cellar item already exists
    cellar = CellarItem.objects.filter(user_id=user_id).filter(cellar_wine_pk=wine.pk)

    if cellar:
        return redirect('update_cellar', cellar[0].pk)

    elif request.method == 'POST':

            quantity = request.POST.get('quantity_onhand')
            if quantity == "":
                quantity = 0

            print(quantity)

            messages.error(request, (
                f'{wine.name} successfully added to your cellar!')
            )

            new_cellar_item = CellarItem(
                cellar_wine_pk=wine,
                user_id=request.user.pk,
                quantity_onhand=quantity
            )
            new_cellar_item.save()

            return redirect('cellar')
        
    template = 'cellar/add_to_cellar.html'
    context = {
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)


@login_required
def update_cellar(request, item_id):
    """ Update the cellar item parameters """

    cellar_item = get_object_or_404(CellarItem, pk=item_id)
    wine = get_object_or_404(Wine, pk=cellar_item.cellar_wine_pk.pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=cellar_item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated quantity for {wine.name}')
            return redirect('cellar')
        else:
            messages.error(request, 'Failed to update cellar item. Please ensure the form is valid.')
    else:
        form = ItemForm(instance=cellar_item)
        messages.info(request, f'This item is already in your cellar. Edit {wine.name}')


    template = 'cellar/update_cellar.html'
    context = {
        'cellar_item': cellar_item,
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)


@login_required
def remove_from_cellar(request, item_id):
    """ Remove item from cellar """
    """ from Code Institute, Django Module https://codeinstitute.net/global/ """
    try:
        cellar_item = get_object_or_404(CellarItem, pk=item_id)
        cellar_item.delete()

        return HttpResponse(status=200)

    except Exception as e:
            return HttpResponse(status=500)