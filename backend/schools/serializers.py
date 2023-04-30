from rest_framework import serializers

from .models import SchoolModel


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SchoolModel
        fields = [
            "id",
            "name",
            "coordinates",
        ]
