from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import CellarItem
from products.models import Wine

def cellar_contents(request):
    """ Create the cellar context so cellar data are avaiable across all apps """
    
    cellar_items = []
    cellar_total = 0
    product_count = 0
    user_id = 34
    cellar = CellarItem.objects.all()
    cellar = cellar.filter(cellar_user_pk=user_id)

    for item in cellar:
        pk = item.cellar_wine_pk
        product = get_object_or_404(Wine, name=pk)
        cellar_total += item.quantity_onhand * product.price
        product_count += item.quantity_onhand
        cellar_items.append({
            'item_id': item.cellar_wine_pk,
            'quantity': item.quantity_onhand,
            'product': product,
        })
    
    context = {
        'cellar_items': cellar_items,
        'cellar_total': cellar_total,
        'product_count': product_count,
    }

    return context