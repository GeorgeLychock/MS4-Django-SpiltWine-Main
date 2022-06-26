from django import forms
from .models import CellarItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = CellarItem
        fields = ['quantity_onhand']
