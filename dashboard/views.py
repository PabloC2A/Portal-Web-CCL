from django.shortcuts import render

# Create your views here.

def dashboard_socio(request):
    return render(request, 'dashboard/socio/dashboard_Socio.html')


def socio_reservas(request):
    return render(request, 'dashboard/socio/socio_reservas.html')

def socio_convenios(request):
    return render(request, 'dashboard/socio/socio_convenios.html')

def socio_noticias(request):
    return render(request, 'dashboard/socio/socio_noticias.html')

def socio_notificaciones(request):
    return render(request, 'dashboard/socio/socio_notificaciones.html')

def socio_configuracion(request):
    return render(request, 'dashboard/socio/socio_configuracion.html')

def socio_soporte(request):
    return render(request, 'dashboard/socio/socio_soporte.html')




def dashboard_empleado(request):
    return render(request, 'dashboard/empleado/dashboard_Empleado.html')

def empleado_usuarios(request):
    return render(request, 'dashboard/empleado/empleado_usuarios.html')

def empleado_solicitudes_afiliacion(request):
    return render(request, 'dashboard/empleado/empleado_solicitudes_afiliacion.html')

def empleado_convenios(request):
    return render(request, 'dashboard/empleado/empleado_convenios.html')

def empleado_espacios_servicios(request):
    return render(request, 'dashboard/empleado/empleado_espacios_servicios.html')

def empleado_noticias_eventos(request):
    return render(request, 'dashboard/empleado/empleado_noticias_eventos.html')

def empleado_metricas(request):
    return render(request, 'dashboard/empleado/empleado_metricas.html')

def empleado_configuracion(request):
    return render(request, 'dashboard/empleado/empleado_configuracion.html')

def empleado_soporte(request):
    return render(request, 'dashboard/empleado/empleado_soporte.html')