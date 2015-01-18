from django.contrib import admin
from app.models import Provider
# Register your models here.

class ProviderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                              {'fields': ['name']}),
        ('Administrative Contact',          {'fields': ['admin_firstname2','admin_lastname2']}),
        ('Details',          {'fields': ['logo', 'URL']}),
        ('Address',          {'fields': ['street','city','zipcode']}),
        ('Geocode',          {'fields': ['latitude','longitude']}),
        ('Characteristics',          {'fields': ['characteristics']}),
    ]

admin.site.register(Provider, ProviderAdmin)