from django.contrib import admin

from .models import MapElementModel, MapLayerModel


@admin.register(MapLayerModel)
class MapLayerModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(MapElementModel)
class MapElementModelAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "layer")
