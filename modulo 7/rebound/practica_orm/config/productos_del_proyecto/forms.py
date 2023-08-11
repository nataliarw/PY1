from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):  # modelform para que se enlace con el modelo
    class Meta:  # para establecer las caracteristicas del formulario
        model = Producto  # modelo al que pertenece el formulario
        fields = ['nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabrica']  # campos del formulario
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio $',
            'f_vencimiento': 'Fecha de Vencimiento',
            'fabrica': 'Fábrica'

        }
        widgets = {  # caracteristicas de los campos
            'nombre': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'f_vencimiento': forms.DateInput(attrs={'class': 'form-control w-100', 'type': 'date'}),
            'fabrica': forms.Select(attrs={'class': 'form-control w-100'})

        }