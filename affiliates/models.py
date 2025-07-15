from django.db import models
from django.utils.translation import gettext_lazy as _


def obtener_ruta_adjunto_persona_natural(instancia, nombre_archivo):
    return f"afiliados/persona_natural/{instancia.id}/{nombre_archivo}"


def obtener_ruta_adjunto_persona_juridica(instancia, nombre_archivo):
    return f"afiliados/persona_juridica/{instancia.id}/{nombre_archivo}"


class SolicitudAfiliacion(models.Model):
    class EstadoSolicitud(models.TextChoices):
        PENDIENTE = "PENDIENTE", _("Pendiente")
        APROBADO = "APROBADO", _("Aprobado")
        RECHAZADO = "RECHAZADO", _("Rechazado")

    estado = models.CharField(
        max_length=10,
        choices=EstadoSolicitud.choices,
        default=EstadoSolicitud.PENDIENTE,
        verbose_name=_("Estado"),
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Fecha de Creación")
    )
    fecha_ultima_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name=_("Última Actualización")
    )

    class Meta:
        verbose_name = _("Solicitud de Afiliación")
        verbose_name_plural = _("Solicitudes de Afiliación")
        ordering = ["-fecha_creacion"]

    def __str__(self):
        if hasattr(self, "solicitudpersonanatural"):
            return str(self.solicitudpersonanatural)
        if hasattr(self, "solicitudpersonajuridica"):
            return str(self.solicitudpersonajuridica)
        return f"Solicitud Genérica #{self.id}"


class SolicitudPersonaNatural(SolicitudAfiliacion):
    cedula = models.CharField(max_length=10, unique=True, verbose_name=_("Cédula"))
    ruc = models.CharField(
        max_length=13, unique=True, blank=True, null=True, verbose_name=_("RUC")
    )
    nombres = models.CharField(max_length=100, verbose_name=_("Nombres"))
    apellidos = models.CharField(max_length=100, verbose_name=_("Apellidos"))
    correo_electronico = models.EmailField(verbose_name=_("Correo Electrónico"))
    numero_celular = models.CharField(max_length=20, verbose_name=_("Celular"))
    archivo_cedula = models.FileField(
        upload_to=obtener_ruta_adjunto_persona_natural,
        verbose_name=_("Archivo de Cédula"),
    )
    archivo_ruc = models.FileField(
        upload_to=obtener_ruta_adjunto_persona_natural,
        blank=True,
        null=True,
        verbose_name=_("Archivo de RUC"),
    )

    class Meta:
        verbose_name = _("Solicitud de Persona Natural")
        verbose_name_plural = _("Solicitudes de Personas Naturales")

    def __str__(self):
        return f"Solicitud (Natural): {self.nombres} {self.apellidos}"


class SolicitudPersonaJuridica(SolicitudAfiliacion):
    ruc_empresa = models.CharField(
        max_length=13, unique=True, verbose_name=_("RUC de la Empresa")
    )
    razon_social = models.CharField(max_length=255, verbose_name=_("Razón Social"))
    nombre_comercial = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Nombre Comercial")
    )
    direccion = models.CharField(max_length=255, verbose_name=_("Dirección"))
    logotipo_empresa = models.ImageField(
        upload_to=obtener_ruta_adjunto_persona_juridica, verbose_name=_("Logotipo")
    )
    cedula_representante_legal = models.CharField(
        max_length=10, verbose_name=_("Cédula del Rep. Legal")
    )
    nombre_completo_representante_legal = models.CharField(
        max_length=200, verbose_name=_("Nombre del Rep. Legal")
    )
    correo_electronico_representante_legal = models.EmailField(
        verbose_name=_("Email del Rep. Legal")
    )
    celular_representante_legal = models.CharField(
        max_length=20, verbose_name=_("Celular del Rep. Legal")
    )
    archivo_ruc_empresa = models.FileField(
        upload_to=obtener_ruta_adjunto_persona_juridica,
        verbose_name=_("Archivo RUC Empresa"),
    )
    archivo_escritura_constitucion = models.FileField(
        upload_to=obtener_ruta_adjunto_persona_juridica,
        verbose_name=_("Archivo Escritura"),
    )
    archivo_cedula_representante = models.FileField(
        upload_to=obtener_ruta_adjunto_persona_juridica,
        verbose_name=_("Archivo Cédula Rep."),
    )
    numeros_contacto_whatsapp = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("WhatsApp")
    )
    url_sitio_web = models.URLField(blank=True, null=True, verbose_name=_("Sitio Web"))

    class Meta:
        verbose_name = _("Solicitud de Persona Jurídica")
        verbose_name_plural = _("Solicitudes de Personas Jurídicas")

    def __str__(self):
        return f"Solicitud (Jurídica): {self.razon_social}"
