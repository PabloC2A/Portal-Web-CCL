from django.urls import path
from . import views

app_name = 'gestionusers'

urlpatterns = [
    path("usuarios/", views.empleado_usuarios, name="empleado_usuarios"),
    path("usuarios/crear/", views.crear_usuario, name="crear_usuario"),
]
