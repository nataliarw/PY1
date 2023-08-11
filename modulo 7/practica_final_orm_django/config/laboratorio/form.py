from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Laboratorio


class LaboratorioForm(forms.ModelForm):  # modelform para que se enlace con el modelo


    class Meta:  # para establecer las caracteristicas del formulario
        model = Laboratorio  # modelo al que pertenece el formulario
        fields = ['nombre', 'ciudad', 'pais']  # campos del formulario
        labels = {
            'nombre': 'Nombre',
            'ciudad': 'Ciudad',
            'pais': 'Pais'
        }
        widgets = {  # caracteristicas de los campos
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'})
        }
