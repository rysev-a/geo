from rest_framework import serializers

from .models import MapElementModel, MapLayerModel


class MapLayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapLayerModel
        fields = [
            "id",
            "name",
        ]


class MapElementSerializer(serializers.HyperlinkedModelSerializer):
    layer = MapLayerSerializer(read_only=True)

    class Meta:
        model = MapElementModel
        fields = ["id", "name", "layer", "longitude", "latitude"]
