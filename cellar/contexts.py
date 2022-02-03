from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Wine

def cellar_contents(request):
    """ Create the cellar context so cellar data are avaiable across all apps """
    """ from Code Institute, Django Module https://codeinstitute.net/global/ """
    
    cellar_items = []
    total = 0
    product_count = 0
    cellar = request.session.get('cellar', {})

    for item_id, quantity in cellar.items():
        product = get_object_or_404(Wine, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cellar_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cellar_items': cellar_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context