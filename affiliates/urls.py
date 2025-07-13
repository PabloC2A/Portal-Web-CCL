from django.urls import path
from . import views

urlpatterns = [
    path("afiliate", views.afiliacion, name="afiliacion"),
]
