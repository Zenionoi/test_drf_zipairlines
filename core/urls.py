from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/airplanes/", include("airplanes.urls", namespace="airplanes")),
    path("__debug__/", include("debug_toolbar.urls")),
]
