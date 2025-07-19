# gestionusers/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model() # Obtiene tu modelo de usuario personalizado si lo tienes, o el User por defecto

class CustomUserCreationForm(UserCreationForm):
    # Puedes personalizar los campos aquí si tu modelo de usuario tiene campos adicionales
    # o si quieres cambiar el orden, añadir validators, etc.
    class Meta(UserCreationForm.Meta):
        model = User
        # Define los campos que quieres en el formulario de creación.
        # Por defecto UserCreationForm tiene username y password.
        # Puedes añadir email, first_name, last_name, etc. si están en tu modelo User.
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'is_staff', 'is_active') # Ejemplo de campos adicionales
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # Añade clases de Bootstrap a los widgets por defecto
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}), # Nota: UserCreationForm maneja los campos de password automáticamente
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añade la clase 'form-control' a los campos de password si no están ya
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields # O puedes listar campos específicos