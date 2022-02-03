from django.http import HttpResponse
from django.shortcuts import render, redirect


def view_cellar(request):
    """ View contents of the user's cellar """

    return render(request, 'cellar/cellar.html')


def add_to_cellar(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    """ from Code Institute, Django Module https://codeinstitute.net/global/ """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cellar = request.session.get('cellar', {})

    if item_id in list(cellar.keys()):
        cellar[item_id] += quantity
    else:
        cellar[item_id] = quantity

    request.session['cellar'] = cellar
    return redirect(redirect_url)


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