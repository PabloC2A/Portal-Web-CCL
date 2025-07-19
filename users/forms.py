from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class FormularioCrearUsuario(UserCreationForm):
    # Definimos los campos aquí para tener control total sobre ellos
    first_name = forms.CharField(
        required=True,
        label="Nombres",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '})
    )
    last_name = forms.CharField(
        required=True,
        label="Apellidos",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '})
    )
    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' '})
    )
    rol = forms.ChoiceField(
        choices=(("socio", "Socio"), ("empleado", "Empleado")),
        required=True,
        label="Rol",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "rol")
        # Personalizamos el campo 'username' que viene de Django
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
        }
        labels = {
            'username': _('Cédula (será el nombre de usuario)'),
        }
        help_texts = {
            'username': _('Obligatorio. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.'),
        }

    # Sobrescribimos los campos de contraseña para traducirlos y estilizarlos
    def __init__(self, *args, **kwargs):
        super(FormularioCrearUsuario, self).__init__(*args, **kwargs)

        # Campo Contraseña
        self.fields['password2'].label = "Contraseña"
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': ' '})
        self.fields['password2'].help_text = _(
            "Tu contraseña debe contener al menos 8 caracteres y no puede ser demasiado común ni completamente numérica."
        )

        # Campo Confirmar Contraseña
        self.fields['password1'].label = "Confirmar Contraseña"
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': ' '})
        self.fields['password1'].help_text = _("Introduce la misma contraseña de antes para verificar.")


class FormularioEditarUsuario(forms.ModelForm):
    """
    Formulario para actualizar los datos de un usuario existente.
    """
    OPCIONES_ROL = (
        ("socio", "Socio"),
        ("empleado", "Empleado"),
    )
    rol = forms.ChoiceField(
        choices=OPCIONES_ROL,
        required=True,
        label="Rol del Usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    is_active = forms.BooleanField(
        required=False,
        label="¿Cuenta activa?",
        widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'})
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_active", "rol"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }