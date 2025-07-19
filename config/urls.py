from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("", include("affiliates.urls")),
    path("dashboard/", include("dashboard.urls")),
]
