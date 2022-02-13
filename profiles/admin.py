from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name', 'email','first_name', 'last_name',)

    fields = ('full_name', 'first_name', 'last_name', 'email', 'default_phone_number', 'default_country',
              'default_postcode', 'default_town_or_city', 'default_street_address1',
              'default_street_address2', 'default_county',)

    list_display = ('full_name', 'first_name', 'last_name', 'email', 'default_phone_number', 'default_town_or_city', 'default_country',
              'default_postcode',)

    ordering = ('last_name',)

admin.site.register(UserProfile, UserProfileAdmin)
