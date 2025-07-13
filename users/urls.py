from django.urls import path
from . import views

urlpatterns = [
    path("user/login", views.login, name="login"),

    # Ruta para el Paso 1: Solicitar correo
    path("user/change_password/", views.change_password, name="change_password"),
    
    # Ruta para el Paso 2: Verificar código
    path("user/verify_code/", views.password_verify_code, name="verify_code"),

    # Ruta para el Paso 3: Ingresar nueva contraseña
    path("user/password_reset_confirm/", views.password_reset_confirm, name="password_reset_confirm"),
]

