from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("", include("affiliates.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("dashboard/", include("gestionusers.urls")),
    path("dashboard/", include("solicitudafiliantes.urls")),

]
