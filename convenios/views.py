from django.shortcuts import render
from users.decorators import empleado_required


@empleado_required
def empleado_convenios(request):
    return render(request, "convenios/empleado_convenios.html")
