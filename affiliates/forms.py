from django import forms


class FormularioAfiliacion(forms.Form):
    TIPO_SOLICITANTE_CHOICES = [
        ("natural", "Persona Natural"),
        ("juridica", "Persona Jurídica"),
    ]

    tipo_solicitante = forms.ChoiceField(
        choices=TIPO_SOLICITANTE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )

    # Campos naturales
    natural_cedula = forms.CharField(required=False)
    natural_ruc = forms.CharField(required=False)
    natural_nombres = forms.CharField(required=False)
    natural_apellidos = forms.CharField(required=False)
    natural_email = forms.EmailField(required=False)
    natural_celular = forms.CharField(required=False)
    natural_cedula_file = forms.FileField(required=False)
    natural_ruc_file = forms.FileField(required=False)

    # Campos jurídicos
    juridica_ruc_empresa = forms.CharField(required=False)
    juridica_razon_social = forms.CharField(required=False)
    juridica_nombre_comercial = forms.CharField(required=False)
    juridica_direccion = forms.CharField(required=False)
    juridica_logo_file = forms.ImageField(required=False)
    juridica_rep_legal_cedula = forms.CharField(required=False)
    juridica_rep_legal_nombres = forms.CharField(required=False)
    juridica_rep_legal_apellidos = forms.CharField(required=False)
    juridica_rep_legal_email = forms.EmailField(required=False)
    juridica_rep_legal_celular = forms.CharField(required=False)
    juridica_ruc_file = forms.FileField(required=False)
    juridica_escritura_file = forms.FileField(required=False)
    juridica_cedula_rep_file = forms.FileField(required=False)
    juridica_whatsapp = forms.CharField(required=False)
    juridica_website = forms.URLField(required=False)

    def clean(self):
        cleaned = super().clean()
        tipo = cleaned.get("tipo_solicitante")

        if not tipo:
            self.add_error(
                "tipo_solicitante", "Debes seleccionar un tipo de solicitante."
            )
            return cleaned

        requeridos = {
            "natural": [
                "natural_cedula",
                "natural_nombres",
                "natural_apellidos",
                "natural_email",
                "natural_celular",
                "natural_cedula_file",
            ],
            "juridica": [
                "juridica_ruc_empresa",
                "juridica_razon_social",
                "juridica_direccion",
                "juridica_logo_file",
                "juridica_rep_legal_cedula",
                "juridica_rep_legal_nombres",
                "juridica_rep_legal_apellidos",
                "juridica_rep_legal_email",
                "juridica_ruc_file",
                "juridica_escritura_file",
                "juridica_cedula_rep_file",
            ],
        }

        for field in requeridos.get(tipo, []):
            if not cleaned.get(field):
                self.add_error(field, "Este campo es obligatorio.")

        return cleaned
