from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def is_empleado(user):
    """
    Verifica si el usuario es un empleado (staff).
    """
    return user.is_authenticated and user.is_staff

@user_passes_test(is_empleado, login_url="login")
def empleado_usuarios(request):
    return render(request, "gestionusers/empleado_usuarios.html")

@user_passes_test(is_empleado, login_url="login")
def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Usuario creado exitosamente', 'user_id': user.id})
            return redirect('gestionusers:empleado_usuarios')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            return render(request, "gestionusers/empleado_usuarios.html", {'form': form})
    else: # GET request, usualmente no se accede directamente
        form = CustomUserCreationForm()
        return redirect('gestionusers:empleado_usuarios') # Redirige a la lista si se accede directamente

@user_passes_test(is_empleado, login_url="login")
def editar_usuario(request, pk):
    user_instance = get_object_or_404(User, pk=pk)
    
    # Asume que tienes un formulario CustomUserChangeForm para la edición
    # Si no lo tienes, puedes usar CustomUserCreationForm o crear uno nuevo
    from .forms import CustomUserChangeForm # Asegúrate de importar esto

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': f'Usuario {user_instance.username} actualizado exitosamente'})
            return redirect('gestionusers:empleado_usuarios')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            # Si no es AJAX, podrías re-renderizar un modal o redirigir con un mensaje
            return render(request, "gestionusers/empleado_usuarios.html", {'edit_form': form}) # Pasar form con errores
    else: # GET request
        form = CustomUserChangeForm(instance=user_instance)
        # Si la petición es AJAX y quiere el HTML del formulario para el modal
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Solo se renderiza el contenido del modal (el formulario)
            html_form = render_to_string('gestionusers/form_usuarioEdit.html', {'edit_form': form}, request=request)
            return JsonResponse({'html_form': html_form})
        
        # Si no es AJAX, y se accede directamente, puede redirigir
        return redirect('gestionusers:empleado_usuarios')

@user_passes_test(is_empleado, login_url="login")
def usuario_detalles(request, pk):
    user_instance = get_object_or_404(User, pk=pk)
    
    # Prepara los datos del usuario para devolverlos como JSON
    details = {
        'cedula': getattr(user_instance, 'cedula', 'N/A'), # Asumiendo que el User tiene un campo 'cedula'
        'nombre_completo': user_instance.get_full_name() or user_instance.username,
        'email': user_instance.email,
        'rol': 'Administrador' if user_instance.is_superuser else ('Empleado' if user_instance.is_staff else 'Socio'), # Lógica de rol simplificada
        'estado': 'Activo' if user_instance.is_active else 'Inactivo',
        'ultima_actualizacion': user_instance.date_joined.strftime('%d/%b/%Y %H:%M') if user_instance.date_joined else 'N/A', # O user_instance.last_login
        # Añade aquí cualquier otro detalle que quieras mostrar
    }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(details)
    
    # Si no es AJAX, redirige o maneja como una página normal (menos común para un modal de detalles)
    return redirect('gestionusers:empleado_usuarios') 