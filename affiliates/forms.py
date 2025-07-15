from django import forms


class FormularioAfiliacion(forms.Form):
    tipo_solicitante = forms.ChoiceField(
        choices=[("natural", "Persona Natural"), ("juridica", "Persona Jurídica")],
        widget=forms.RadioSelect,
        required=True,
    )

    # --- Campos para Persona Natural ---
    natural_cedula = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    natural_ruc = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    natural_nombres = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    natural_apellidos = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    natural_email = forms.EmailField(
        required=False, widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    natural_celular = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    natural_cedula_file = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )
    natural_ruc_file = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )

    # --- Campos para Persona Jurídica ---
    juridica_ruc_empresa = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_razon_social = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_nombre_comercial = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_direccion = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_logo_file = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )
    juridica_rep_legal_cedula = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_rep_legal_nombres = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_rep_legal_apellidos = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_rep_legal_email = forms.EmailField(
        required=False, widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    juridica_rep_legal_celular = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_ruc_file = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )
    juridica_escritura_file = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )
    juridica_cedula_rep_file = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "custom-file-input"})
    )
    juridica_whatsapp = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    juridica_website = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={"class": "form-control", "placeholder": "https://ejemplo.com"}
        ),
    )

    def clean(self):
        datos_limpios = super().clean()
        tipo = datos_limpios.get("tipo_solicitante")
        if not tipo:
            self.add_error(
                "tipo_solicitante", "Debes seleccionar un tipo de solicitante."
            )
            return

        if tipo == "natural":
            campos_requeridos = [
                "natural_cedula",
                "natural_nombres",
                "natural_apellidos",
                "natural_email",
                "natural_celular",
                "natural_cedula_file",
            ]
        else:  # tipo == 'juridica'
            campos_requeridos = [
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
            ]

        for campo in campos_requeridos:
            if not datos_limpios.get(campo):
                self.add_error(campo, "Este campo es obligatorio.")

        return datos_limpios
