from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioAfiliacion
from .models import SolicitudPersonaNatural, SolicitudPersonaJuridica
from users.decorators import empleado_required


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
    return render(request, "affiliates/empleado_solicitudes_afiliacion.html")
