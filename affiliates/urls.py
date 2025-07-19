from django.urls import path
from . import views

urlpatterns = [
    path("afiliate/", views.crear_solicitud_afiliacion, name="afiliacion"),   
    path("afiliate/gestionAfiliaciones", views.empleado_solicitudes_afiliacion, name="empleado_solicitudes_afiliacion"),   
]
