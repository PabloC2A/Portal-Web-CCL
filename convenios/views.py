from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def is_empleado(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_empleado, login_url="login")
def empleado_convenios(request):
    return render(request, "convenios/empleado_convenios.html")