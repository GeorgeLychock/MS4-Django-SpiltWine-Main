from django.contrib import admin
from .models import Wine, Appellation, Region, WineType, Brand, CountryState, Varietal, Style, Body

class WineAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'country_state',
        'price',
        'img_file_name',
    )

    ordering = ('name',)

# Register your models here.
admin.site.register(Appellation)
admin.site.register(Region)
admin.site.register(WineType)
admin.site.register(Brand)
admin.site.register(CountryState)
admin.site.register(Varietal)
admin.site.register(Style)
admin.site.register(Body)
admin.site.register(Wine, WineAdmin)
