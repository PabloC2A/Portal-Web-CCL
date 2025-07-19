from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.
def is_empleado(user):
    """
    Verifica si el usuario es un empleado (staff).
    """
    return user.is_authenticated and user.is_staff


@user_passes_test(is_empleado, login_url="login")
def empleado_solicitudes_afiliacion(request):
    return render(request, "solicitudafiliantes/empleado_solicitudes_afiliacion.html")