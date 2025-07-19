from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string

from users.decorators import empleado_required
from .forms import FormularioAfiliacion
from .models import (
    SolicitudPersonaNatural,
    SolicitudPersonaJuridica,
    SolicitudAfiliacion,
)


def crear_solicitud_afiliacion(request):
    if request.method == "POST":
        form = FormularioAfiliacion(request.POST, request.FILES)
        if form.is_valid():
            datos = form.cleaned_data
            if datos["tipo_solicitante"] == "natural":
                SolicitudPersonaNatural.objects.create(
                    cedula=datos["natural_cedula"],
                    ruc=datos.get("natural_ruc"),
                    nombres=datos["natural_nombres"],
                    apellidos=datos["natural_apellidos"],
                    correo_electronico=datos["natural_email"],
                    numero_celular=datos["natural_celular"],
                    archivo_cedula=datos["natural_cedula_file"],
                    archivo_ruc=datos.get("natural_ruc_file"),
                )
            elif datos["tipo_solicitante"] == "juridica":
                nombre_rep = f"{datos['juridica_rep_legal_nombres']} {datos['juridica_rep_legal_apellidos']}"
                SolicitudPersonaJuridica.objects.create(
                    ruc_empresa=datos["juridica_ruc_empresa"],
                    razon_social=datos["juridica_razon_social"],
                    nombre_comercial=datos.get("juridica_nombre_comercial"),
                    direccion=datos["juridica_direccion"],
                    logotipo_empresa=datos["juridica_logo_file"],
                    cedula_representante_legal=datos["juridica_rep_legal_cedula"],
                    nombre_completo_representante_legal=nombre_rep,
                    correo_electronico_representante_legal=datos[
                        "juridica_rep_legal_email"
                    ],
                    celular_representante_legal=datos["juridica_rep_legal_celular"],
                    archivo_ruc_empresa=datos["juridica_ruc_file"],
                    archivo_escritura_constitucion=datos["juridica_escritura_file"],
                    archivo_cedula_representante=datos["juridica_cedula_rep_file"],
                    numeros_contacto_whatsapp=datos.get("juridica_whatsapp"),
                    url_sitio_web=datos.get("juridica_website"),
                )

            messages.success(
                request, "¡Tu solicitud de afiliación ha sido enviada con éxito!"
            )

            return redirect("afiliacion")
    else:
        form = FormularioAfiliacion()

    return render(request, "affiliates/afiliacion.html", {"form": form})


@empleado_required
def empleado_solicitudes_afiliacion(request):
    """Muestra la lista de todas las solicitudes de afiliación."""
    listado_solicitudes = SolicitudAfiliacion.objects.select_related(
        "solicitudpersonanatural", "solicitudpersonajuridica"
    ).all()
    contexto = {"solicitudes": listado_solicitudes}
    return render(request, "affiliates/empleado_solicitudes_afiliacion.html", contexto)


@empleado_required
def detalles_solicitud_api(request, pk):
    """Devuelve los detalles de una solicitud específica en formato JSON."""
    solicitud = get_object_or_404(
        SolicitudAfiliacion.objects.select_related(
            "solicitudpersonanatural", "solicitudpersonajuridica"
        ),
        pk=pk,
    )
    datos = {
        "id": solicitud.id,
        "estado": solicitud.estado,
        "estado_display": solicitud.get_estado_display(),
        "fecha_envio": solicitud.fecha_creacion.strftime("%d/%m/%Y a las %H:%M"),
        "documentos": [],
    }
    if hasattr(solicitud, "solicitudpersonanatural"):
        natural = solicitud.solicitudpersonanatural
        datos.update(
            {
                "tipo": "natural",
                "solicitante": {
                    "nombre": f"{natural.nombres} {natural.apellidos}",
                    "cedula_ruc": natural.cedula,
                    "email": natural.correo_electronico,
                    "telefono": natural.numero_celular,
                },
            }
        )
        datos["documentos"].append(
            {"nombre": "Cédula", "url": natural.archivo_cedula.url}
        )
        if natural.archivo_ruc:
            datos["documentos"].append(
                {"nombre": "RUC", "url": natural.archivo_ruc.url}
            )
    elif hasattr(solicitud, "solicitudpersonajuridica"):
        juridica = solicitud.solicitudpersonajuridica
        datos.update(
            {
                "tipo": "juridica",
                "solicitante": {
                    "nombre": juridica.nombre_completo_representante_legal,
                    "cedula_ruc": juridica.cedula_representante_legal,
                    "email": juridica.correo_electronico_representante_legal,
                    "telefono": juridica.celular_representante_legal,
                },
                "empresa": {
                    "razon_social": juridica.razon_social,
                    "nombre_comercial": juridica.nombre_comercial or "N/A",
                    "actividad": "No especificada",
                    "direccion": juridica.direccion,
                },
            }
        )
        datos["documentos"].extend(
            [
                {"nombre": "RUC Empresa", "url": juridica.archivo_ruc_empresa.url},
                {
                    "nombre": "Escritura",
                    "url": juridica.archivo_escritura_constitucion.url,
                },
                {
                    "nombre": "Cédula Rep. Legal",
                    "url": juridica.archivo_cedula_representante.url,
                },
            ]
        )
    return JsonResponse(datos)


@empleado_required
def aprobar_solicitud(request, pk):
    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "Método no permitido."}, status=405
        )
    solicitud = get_object_or_404(
        SolicitudAfiliacion.objects.select_related(
            "solicitudpersonanatural", "solicitudpersonajuridica"
        ),
        pk=pk,
    )
    if solicitud.estado != "PENDIENTE":
        return JsonResponse(
            {"status": "error", "message": "Esta solicitud ya fue procesada."},
            status=400,
        )
    if hasattr(solicitud, "solicitudpersonanatural"):
        email = solicitud.solicitudpersonanatural.correo_electronico
        first_name = solicitud.solicitudpersonanatural.nombres
        last_name = solicitud.solicitudpersonanatural.apellidos
    elif hasattr(solicitud, "solicitudpersonajuridica"):
        email = (
            solicitud.solicitudpersonajuridica.correo_electronico_representante_legal
        )
        partes_nombre = solicitud.solicitudpersonajuridica.nombre_completo_representante_legal.split(
            " "
        )
        first_name, last_name = partes_nombre[0], " ".join(partes_nombre[1:])
    if User.objects.filter(email=email).exists():
        return JsonResponse(
            {"status": "error", "message": f"El correo '{email}' ya está en uso."},
            status=400,
        )
    username_base = f"{first_name}{last_name}".replace(" ", "").lower()
    username_final, contador = username_base, 1
    while User.objects.filter(username=username_final).exists():
        username_final = f"{username_base}{contador}"
        contador += 1
    contraseña_temporal = get_random_string(10)
    User.objects.create_user(
        username=username_final,
        email=email,
        password=contraseña_temporal,
        first_name=first_name,
        last_name=last_name,
    )
    send_mail(
        "¡Solicitud de afiliación aprobada!",
        f"Hola {first_name},\n\nTu solicitud ha sido aprobada. Tus credenciales son:\nUsuario: {username_final}\nContraseña Temporal: {contraseña_temporal}",
        "noreply@ccl.com",
        [email],
        fail_silently=False,
    )
    solicitud.estado = "APROBADO"
    solicitud.save()
    messages.success(
        request,
        f'Solicitud #{solicitud.id} aprobada. Usuario "{username_final}" creado.',
    )
    return JsonResponse({"status": "success"})


@empleado_required
def rechazar_solicitud(request, pk):
    """Cambia el estado de una solicitud a 'Rechazado' y devuelve JSON."""
    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "Método no permitido."}, status=405
        )

    solicitud = get_object_or_404(SolicitudAfiliacion, pk=pk)
    if solicitud.estado != "PENDIENTE":
        return JsonResponse(
            {"status": "error", "message": "Esta solicitud ya fue procesada."},
            status=400,
        )

    solicitud.estado = "RECHAZADO"
    solicitud.save()
    messages.warning(request, f"La solicitud #{solicitud.id} ha sido rechazada.")
    return JsonResponse({"status": "success"})
