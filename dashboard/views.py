from django.shortcuts import render

# Create your views here.

def dashboard_socio(request):
    # The path should be relative to the 'templates' directory
    return render(request, 'dashboard/socio/dashboard_Socio.html')

def dashboard_empleado(request):
    # Correcting this path as well, based on your file structure
    return render(request, 'dashboard/empleado/dashboard_Empleado.html')