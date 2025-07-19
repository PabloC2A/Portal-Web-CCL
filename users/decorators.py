from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test


def socio_check(user):
    """
    Regla de permiso para Socios.
    Debe estar autenticado, activo y NO ser staff.
    """
    if not user.is_authenticated:
        return False

    if not user.is_active:
        raise PermissionDenied("Tu cuenta se encuentra inactiva.")

    if user.is_staff:
        raise PermissionDenied("Esta página es exclusiva para socios.")

    return True


def empleado_check(user):
    """
    Regla de permiso para Empleados.
    Debe estar autenticado, activo y ser staff.
    """
    if not user.is_authenticated:
        return False

    if not user.is_active:
        raise PermissionDenied("Tu cuenta se encuentra inactiva.")

    if not user.is_staff:
        raise PermissionDenied(
            "No tienes los permisos de empleado para acceder a esta página."
        )

    return True


socio_required = user_passes_test(socio_check, login_url="login")

empleado_required = user_passes_test(empleado_check, login_url="login")
