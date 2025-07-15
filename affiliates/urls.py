from django.urls import path
from . import views

urlpatterns = [
    path("afiliate/", views.crear_solicitud_afiliacion, name="afiliacion"),
]
