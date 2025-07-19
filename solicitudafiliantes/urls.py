from django.urls import path
from . import views

urlpatterns = [
    path("solicitudes-afiliacion/", views.empleado_solicitudes_afiliacion, name="empleado_solicitudes_afiliacion"),
]