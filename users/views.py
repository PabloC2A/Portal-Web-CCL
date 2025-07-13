from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    # Crea una instancia del formulario de autenticación
    form = AuthenticationForm(request, data=request.POST or None)

    # Procesa la solicitud si es POST y verifica si el formulario es válido
    if request.method == "POST" and form.is_valid():
        # Autentica e inicia sesión
        user = form.get_user()
        auth_login(request, user)
        # Respuesta temporal en texto plano
        return HttpResponse(
            "Inicio de sesión exitoso. Puedes acceder a las rutas protegidas."
        )

    # Si es GET o el formulario es inválido, renderiza el formulario
    return render(request, "users/login.html", {"form": form})
