from django.contrib import admin
from django.urls import path, include

from affiliates.views import empleado_solicitudes_afiliacion

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("", include("affiliates.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("dashboard/", include("affiliates.urls")),
    path("dashboard/", include("convenios.urls")),
    path(
        "dashboard/solicitudes-afiliacion/",
        empleado_solicitudes_afiliacion,
        name="gestion_afiliaciones",
    ),
]
