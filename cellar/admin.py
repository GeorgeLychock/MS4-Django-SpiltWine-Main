from django.contrib import admin
from .models import CellarItem


class CellarItemAdmin(admin.ModelAdmin):
    list_display = (
        'cellar_wine_pk',
        'date_added_to_cellar',
        'quantity_onhand',
        'cellar_user_pk',
    )

    ordering = ('date_added_to_cellar',)

admin.site.register(CellarItem, CellarItemAdmin)
