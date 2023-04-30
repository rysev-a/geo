from django.db.models import QuerySet
from rest_framework import routers, viewsets

from .models import MapElementModel
from .serializers import MapElementSerializer


class MapElementViewSet(viewsets.ModelViewSet):
    query: QuerySet
    query_params: dict
    queryset = MapElementModel.objects.all()
    serializer_class = MapElementSerializer
    permission_classes = []


map_router = routers.DefaultRouter()
map_router.register("elements", MapElementViewSet)
