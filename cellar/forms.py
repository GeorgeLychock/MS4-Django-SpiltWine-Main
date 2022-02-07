from django import forms
from .models import CellarItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = CellarItem
        fields = ['cellar_wine_pk', 'cellar_user_pk', 'quantity_onhand']