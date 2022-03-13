from django.contrib import admin
from .models import Wine, Appellation, Region, WineType, WineBrand, CountryState, Varietal, Style, Body, WineAccessoryBrand, WineAccessory, CulinaryBrand, Culinary, Measure

class WineAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'sku',
        'name',
        'country_state',
        'price',
        'image',
        'puid',
    )

    ordering = ('name',)

class WineAccessoryAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'price',
        'image',
        'puid',
    )

    ordering = ('name',)

class CulinaryAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'price',
        'image',
        'puid',
    )

    ordering = ('name',)

# Register your models here.
admin.site.register(Appellation)
admin.site.register(Region)
admin.site.register(WineType)
admin.site.register(WineBrand)
admin.site.register(WineAccessoryBrand)
admin.site.register(CulinaryBrand)
admin.site.register(CountryState)
admin.site.register(Varietal)
admin.site.register(Style)
admin.site.register(Body)
admin.site.register(Measure)
admin.site.register(Wine, WineAdmin)
admin.site.register(WineAccessory, WineAccessoryAdmin)
admin.site.register(Culinary, CulinaryAdmin)