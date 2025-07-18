from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def is_empleado(user):
    """
    Verifica si el usuario es un empleado (staff).
    """
    return user.is_authenticated and user.is_staff


def is_socio(user):
    """
    Verifica si el usuario es un socio.
    """
    if not user.is_authenticated:
        return False
    if user.is_staff:
        # Si es empleado, no tiene permiso para vistas de socio
        raise PermissionDenied
    return True


@user_passes_test(is_socio, login_url="login")
def dashboard_socio(request):
    return render(request, "dashboard/socio/dashboard_Socio.html")


@user_passes_test(is_socio, login_url="login")
def socio_reservas(request):
    return render(request, "dashboard/socio/socio_reservas.html")


@user_passes_test(is_socio, login_url="login")
def socio_convenios(request):
    return render(request, "dashboard/socio/socio_convenios.html")


@user_passes_test(is_socio, login_url="login")
def socio_noticias(request):
    return render(request, "dashboard/socio/socio_noticias.html")


@user_passes_test(is_socio, login_url="login")
def socio_notificaciones(request):
    return render(request, "dashboard/socio/socio_notificaciones.html")


@user_passes_test(is_socio, login_url="login")
def socio_configuracion(request):
    return render(request, "dashboard/socio/socio_configuracion.html")


@user_passes_test(is_socio, login_url="login")
def socio_soporte(request):
    return render(request, "dashboard/socio/socio_soporte.html")


@user_passes_test(is_empleado, login_url="login")
def dashboard_empleado(request):
    return render(request, "dashboard/empleado/dashboard_Empleado.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_usuarios(request):
    return render(request, "dashboard/empleado/empleado_usuarios.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_solicitudes_afiliacion(request):
    return render(request, "dashboard/empleado/empleado_solicitudes_afiliacion.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_convenios(request):
    return render(request, "dashboard/empleado/empleado_convenios.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_espacios_servicios(request):
    return render(request, "dashboard/empleado/empleado_espacios_servicios.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_noticias_eventos(request):
    return render(request, "dashboard/empleado/empleado_noticias_eventos.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_metricas(request):
    return render(request, "dashboard/empleado/empleado_metricas.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_configuracion(request):
    return render(request, "dashboard/empleado/empleado_configuracion.html")


@user_passes_test(is_empleado, login_url="login")
def empleado_soporte(request):
    return render(request, "dashboard/empleado/empleado_soporte.html")