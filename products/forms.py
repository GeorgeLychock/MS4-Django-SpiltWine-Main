from django import forms
from django.forms import TextInput, NumberInput
from .widgets import CustomClearableFileInput
from django.utils.translation import gettext_lazy as _

from .models import Wine, WineBrand, Appellation, Region, WineType, CountryState, Varietal, Style, Body


class ProductForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = ('name', 'vintage', 'brand', 'sku', 'featured', 'image', 'img_url', 
                'has_sizes', 'size', 'measure', 'price', 'description', 
                'country_state', 'region', 'appellation', 'wine_type', 'varietal', 'body', 'style', 
                'abv', 'taste',)
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'enter name'
                }),
            'vintage': NumberInput(attrs={
                'class': "sw-form-input-num",
                "size": "4",
                'placeholder': 'enter vintage',
                'max': 2022,
                'min': 1990
                }),
        }
        help_texts = {
            'vintage': _('Enter a year between 1990 and 2022.'),
        }
        error_messages = {
            'vintage': {
                'max': _('The vintage year is to old.'),
            },
        }


    # custom widget does not work currently
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        brands = WineBrand.objects.all()
        appellations = Appellation.objects.all()
        regions = Region.objects.all()
        winetypes = WineType.objects.all()
        countries = CountryState.objects.all()
        varietals = Varietal.objects.all()
        styles = Style.objects.all()
        body = Body.objects.all()


        friendly_names_brands = [(n.id, n.get_friendly_name()) for n in brands]
        friendly_names_apps = [(n.id, n.get_friendly_name()) for n in appellations]
        friendly_names_regions = [(n.id, n.get_friendly_name()) for n in regions]
        friendly_names_types = [(n.id, n.get_friendly_name()) for n in winetypes]
        friendly_names_countries = [(n.id, n.get_friendly_name()) for n in countries]
        friendly_names_varietals = [(n.id, n.get_friendly_name()) for n in varietals]
        friendly_names_styles = [(n.id, n.get_friendly_name()) for n in styles]
        friendly_names_body = [(n.id, n.get_friendly_name()) for n in body]

        self.fields['brand'].choices = friendly_names_brands
        self.fields['appellation'].choices = friendly_names_apps
        self.fields['region'].choices = friendly_names_regions
        self.fields['wine_type'].choices = friendly_names_types
        self.fields['wine_type'].label = "Wine Types"
        self.fields['country_state'].choices = friendly_names_countries
        self.fields['country_state'].label = "Country/State"
        self.fields['varietal'].choices = friendly_names_varietals
        self.fields['style'].choices = friendly_names_styles
        self.fields['body'].choices = friendly_names_body

        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'border-black rounded-0'