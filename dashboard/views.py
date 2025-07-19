from django.shortcuts import render
from users.decorators import socio_required, empleado_required


@socio_required
def dashboard_socio(request):
    return render(request, "dashboard/socio/dashboard_Socio.html")


@socio_required
def socio_reservas(request):
    return render(request, "dashboard/socio/socio_reservas.html")


@socio_required
def socio_convenios(request):
    return render(request, "dashboard/socio/socio_convenios.html")


@socio_required
def socio_noticias(request):
    return render(request, "dashboard/socio/socio_noticias.html")


@socio_required
def socio_notificaciones(request):
    return render(request, "dashboard/socio/socio_notificaciones.html")


@socio_required
def socio_configuracion(request):
    return render(request, "dashboard/socio/socio_configuracion.html")


@socio_required
def socio_soporte(request):
    return render(request, "dashboard/socio/socio_soporte.html")


@empleado_required  # <-- CORREGIDO
def dashboard_empleado(request):
    return render(request, "dashboard/empleado/dashboard_Empleado.html")


@empleado_required
def empleado_convenios(request):
    return render(request, "dashboard/empleado/empleado_convenios.html")


@empleado_required
def empleado_espacios_servicios(request):
    return render(request, "dashboard/empleado/empleado_espacios_servicios.html")


@empleado_required
def empleado_noticias_eventos(request):
    return render(request, "dashboard/empleado/empleado_noticias_eventos.html")


@empleado_required
def empleado_metricas(request):
    return render(request, "dashboard/empleado/empleado_metricas.html")


@empleado_required
def empleado_configuracion(request):
    return render(request, "dashboard/empleado/empleado_configuracion.html")


@empleado_required
def empleado_soporte(request):
    return render(request, "dashboard/empleado/empleado_soporte.html")
