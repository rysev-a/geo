from django.db.models import QuerySet
from rest_framework import routers, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import SchoolModel
from .serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    query: QuerySet
    query_params: dict
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = []


schools_router = routers.DefaultRouter()
schools_router.register("schools", SchoolViewSet)
