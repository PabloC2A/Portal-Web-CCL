from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .decorators import empleado_required
from .forms import FormularioCrearUsuario, FormularioEditarUsuario


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
    listado_de_usuarios = User.objects.all().order_by("last_name")
    formulario_vacio = FormularioCrearUsuario()
    contexto = {
        "usuarios": listado_de_usuarios,
        "form": formulario_vacio,
        "edit_form": FormularioEditarUsuario(),
    }
    return render(request, "users/empleado_usuarios.html", contexto)


@empleado_required
def crear_usuario(request):
    if request.method != "POST":
        return redirect("gestion_usuarios")

    formulario = FormularioCrearUsuario(request.POST)

    if formulario.is_valid():
        usuario = formulario.save(commit=False)
        rol_seleccionado = formulario.cleaned_data["rol"]
        if rol_seleccionado == "empleado":
            usuario.is_staff = True
        usuario.save()

        messages.success(request, f'¡Usuario "{usuario.username}" creado exitosamente!')
        return redirect("gestion_usuarios")
    else:
        messages.error(request, "No se pudo crear el usuario. Revisa los errores.")
        listado_de_usuarios = User.objects.all().order_by("last_name")
        contexto = {
            "usuarios": listado_de_usuarios,
            "form": formulario,
        }
        return render(request, "users/empleado_usuarios.html", contexto)


@empleado_required
def editar_usuario(request, pk):
    # Obtenemos el usuario específico que se quiere editar o mostramos un error 404
    usuario_a_editar = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        # Si se envía el formulario, lo procesamos
        formulario = FormularioEditarUsuario(request.POST, instance=usuario_a_editar)
        if formulario.is_valid():
            # Actualizamos el rol basado en la selección
            rol_seleccionado = formulario.cleaned_data["rol"]
            usuario_a_editar.is_staff = rol_seleccionado == "empleado"
            formulario.save()

            messages.success(
                request,
                f'¡Usuario "{usuario_a_editar.username}" actualizado correctamente!',
            )
            return redirect("gestion_usuarios")
    else:
        # Si se accede por GET, mostramos el formulario con los datos actuales del usuario
        formulario = FormularioEditarUsuario(instance=usuario_a_editar)
        # Marcamos el 'rol' actual en el formulario para que aparezca preseleccionado
        rol_actual = "empleado" if usuario_a_editar.is_staff else "socio"
        formulario.fields["rol"].initial = rol_actual

    contexto = {"form": formulario, "usuario": usuario_a_editar}
    # Renderizamos una nueva plantilla dedicada a la edición
    return render(request, "users/form_usuarioEdit.html", contexto)


@empleado_required
def usuario_detalles(request):
    return redirect("empleado_usuarios")
