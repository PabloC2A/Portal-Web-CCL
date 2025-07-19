from django.urls import path
from . import views

urlpatterns = [
    path("empleado/convenios/", views.empleado_convenios, name="empleado_convenios"),
]
