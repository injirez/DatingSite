from django.contrib.gis import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Client

@admin.register(Client)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('user', 'name', 'surname', 'gender', 'email', 'photo', 'location')