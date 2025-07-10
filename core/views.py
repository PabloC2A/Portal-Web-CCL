from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def socios(request):
    return render(request, 'core/socios.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def noticias(request):
    return render(request, 'core/noticias.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def afiliacion(request):
    return render(request, 'core/afiliacion.html')

def login(request):
    return render(request, 'core/login.html')
