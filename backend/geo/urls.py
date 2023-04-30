from django.contrib import admin
from django.urls import include, path

from schools.views import schools_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schools/", include(schools_router.urls)),
]
