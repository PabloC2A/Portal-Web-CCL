from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse


def login(request):
    # Crea una instancia del formulario de autenticación
    form = AuthenticationForm(request, data=request.POST or None)

    # Procesa la solicitud si es POST y verifica si el formulario es válido
    if request.method == "POST" and form.is_valid():
        # Autentica e inicia sesión
        user = form.get_user()
        auth_login(request, user)

        # Redirige según el rol del usuario
        if user.is_superuser:
            return redirect("admin:index")
        elif user.is_staff:
            return redirect("dashboard_empleado")
        else:
            return redirect("dashboard_socio")

    # Si es GET o el formulario es inválido, renderiza el formulario
    return render(request, "users/login.html", {"form": form})


def change_password(request):
    # Muestra el Paso 1: Solicitar correo
    return render(request, "users/change_password.html")


def password_verify_code(request):
    # Muestra el Paso 2: Ingresar código
    return render(request, "users/password_verify_code.html")


def password_reset_confirm(request):
    # Muestra el Paso 3: Ingresar nueva contraseña
    return render(request, "users/password_reset_confirm.html")
