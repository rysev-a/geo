from django.db import models


class MapElementModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    layer = models.ForeignKey("map.MapLayerModel", on_delete=models.CASCADE, null=True)
    metadata = models.JSONField(default=dict(), blank=True, null=True)

    def __str__(self):
        return self.name


class MapLayerModel(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
