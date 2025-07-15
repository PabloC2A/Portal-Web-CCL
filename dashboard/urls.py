from django.urls import path
from . import views

urlpatterns = [
    path("socio/", views.dashboard_socio, name="dashboard_socio"),
    path("empleado/", views.dashboard_empleado, name="dashboard_empleado"),
]
