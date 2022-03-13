from django import template


register = template.Library()

@register.filter(name='calc_subtotal_cellar')
def calc_subtotal_cellar(price, quantity):
    if quantity:
        return price * quantity
    else:
        return(' -- ')