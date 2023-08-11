from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Vehiculo
from .admin import VehiculoAdmin


class VehiculoForm(forms.ModelForm):  # modelform para que se enlace con el modelo
    class Meta:  # para establecer las caracteristicas del formulario
        model = Vehiculo  # modelo al que pertenece el formulario
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria',
                  'precio']  # campos del formulario
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'serial_carroceria': 'Serial Carroceria',
            'serial_motor': 'Serial Motor',
            'categoria': 'Categoria',
            'precio': 'Precio $'
        }
        widgets = {  # caracteristicas de los campos
            'marca': forms.Select(),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'serial_motor': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'categoria': forms.Select(),
            'Precio': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'})

        }


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nombre usuario', min_length=5, max_length=150)
    email = forms.EmailField(label='Email')
    confirm_email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'confirm_email', 'password1', 'password2')

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Nombre de usuario ya existe")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email ya registrado")
        return email

    def clean(self):
        email1 = self.cleaned_data['email']
        email2 = self.cleaned_data['confirm_email']
        if email1 and email2 and email1 != email2:
            raise ValidationError("Emails no coinciden")
        return email2

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Contrasenas no coinciden")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
