from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioCrearUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombres")
    last_name = forms.CharField(required=True, label="Apellidos")
    rol = forms.ChoiceField(
        choices=(("socio", "Socio"), ("empleado", "Empleado")),
        required=True,
        label="Rol",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "rol")


class FormularioEditarUsuario(forms.ModelForm):
    """
    Formulario para actualizar los datos de un usuario existente.
    """

    OPCIONES_ROL = (
        ("socio", "Socio"),
        ("empleado", "Empleado"),
    )
    rol = forms.ChoiceField(
        choices=OPCIONES_ROL, required=True, label="Rol del Usuario"
    )

    is_active = forms.BooleanField(required=False, label="¿Cuenta activa?")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_active", "rol"]
