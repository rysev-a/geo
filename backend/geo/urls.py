from django.contrib import admin
from django.urls import include, path

from map.views import map_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/map/", include(map_router.urls)),
]
