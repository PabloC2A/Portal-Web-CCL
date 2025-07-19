from django.urls import path

from users.views import (
    gestionar_usuarios,
    crear_usuario,
    editar_usuario,
    desactivar_usuario,
)
from . import views

urlpatterns = [
    path("socio/", views.dashboard_socio, name="dashboard_socio"),
    path("socio/reservas/", views.socio_reservas, name="socio_reservas"),
    path("socio/convenios/", views.socio_convenios, name="socio_convenios"),
    path("socio/noticias/", views.socio_noticias, name="socio_noticias"),
    path(
        "socio/notificaciones/", views.socio_notificaciones, name="socio_notificaciones"
    ),
    path("socio/configuracion/", views.socio_configuracion, name="socio_configuracion"),
    path("socio/soporte/", views.socio_soporte, name="socio_soporte"),
    path("empleado/", views.dashboard_empleado, name="dashboard_empleado"),
    path(
        "empleado/usuarios/",
        gestionar_usuarios,
        name="gestion_usuarios",
    ),
    path("empleado/usuarios/crear", crear_usuario, name="crear_usuario"),
    path("empleado/usuarios/<int:pk>/editar/", editar_usuario, name="editar_usuario"),
    path(
        "empleado/usuarios/<int:pk>/desactivar/",
        desactivar_usuario,
        name="desactivar_usuario",
    ),
    path("empleado/convenios/", views.empleado_convenios, name="empleado_convenios"),
    path(
        "empleado/espacios-servicios/",
        views.empleado_espacios_servicios,
        name="empleado_espacios_servicios",
    ),
    path(
        "empleado/noticias-eventos/",
        views.empleado_noticias_eventos,
        name="empleado_noticias_eventos",
    ),
    path("empleado/metricas/", views.empleado_metricas, name="empleado_metricas"),
    path(
        "empleado/configuracion/",
        views.empleado_configuracion,
        name="empleado_configuracion",
    ),
    path("empleado/soporte/", views.empleado_soporte, name="empleado_soporte"),
]
