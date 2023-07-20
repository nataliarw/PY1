from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Book


class BookForm(forms.ModelForm):  # modelform para que se enlace con el modelo
    # estructura para validacion  de valoracion sin negativos
    valoracion = forms.IntegerField(
        label='Valoración',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
        help_text='Valoracion entre 0 y 10.000',
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )

    class Meta:  # para establecer las caracteristicas del formulario
        model = Book  # modelo al que pertenece el formulario
        fields = ['titulo', 'autor', 'valoracion']  # campos del formulario
        labels = {
            'titulo': 'Título',
            'autor': 'Autor'
        }
        widgets = {  # caracteristicas de los campos
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            # 'valoracion': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'})
        }
