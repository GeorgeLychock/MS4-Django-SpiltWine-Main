from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import CellarItem
from products.models import Wine


def cellar_contents(request):
    """ Create the cellar context so
        cellar data are avaiable across all apps """

    cellar_items = []
    cellar_total = 0
    cellar_count = 0
    varietal_count = []
    cellar_user = request.user
    cellar = CellarItem.objects.all()
    cellar = cellar.filter(user_id=cellar_user.pk)

    for item in cellar:
        pk = item.cellar_wine_pk
        product = get_object_or_404(Wine, name=pk)
        if not varietal_count.count(product.varietal.friendly_name):
            varietal_count.append(product.varietal.friendly_name)

        # UPDATE NEEDED: need to catch error if price isn't given
        if item.quantity_onhand is not None:
            cellar_total += item.quantity_onhand * product.price
            cellar_count += item.quantity_onhand

        cellar_items.append({
            'item_id': item.pk,
            'quantity': item.quantity_onhand,
            'product': product,
        })

    cellar_contents = {
        'cellar_items': cellar_items,
        'cellar_total': cellar_total,
        'cellar_count': cellar_count,
        'cellar_varietal_count': varietal_count
    }

    return cellar_contents
