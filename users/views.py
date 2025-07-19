from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .decorators import empleado_required


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


def logout(request):
    auth_logout(request)
    return redirect("login")


def change_password(request):
    return render(request, "users/change_password.html")


def password_verify_code(request):
    return render(request, "users/password_verify_code.html")


def password_reset_confirm(request):
    return render(request, "users/password_reset_confirm.html")


@empleado_required
def gestionar_usuarios(request):
    """
    Mostrar la lista de todos los usuarios del sistema
    """
    listado_de_usuarios = User.objects.all().order_by("last_name")
    contexto = {"usuarios": listado_de_usuarios}
    return render(request, "users/empleado_usuarios.html", contexto)


@empleado_required
def crear_usuario(request):
    return redirect("empleado_usuarios")


@empleado_required
def editar_usuario(request):
    return redirect("empleado_usuarios")


@empleado_required
def usuario_detalles(request):
    return redirect("empleado_usuarios")
