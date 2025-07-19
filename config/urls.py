from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from affiliates.views import empleado_solicitudes_afiliacion
from users.views import empleado_usuarios

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
        name="gestion_afiliaciones"
    ),
    path(
        "dashboard/usuarios/",
        empleado_usuarios,
        name="gestion_usuarios" # Le damos un nombre nuevo y claro
    ),

    
]
