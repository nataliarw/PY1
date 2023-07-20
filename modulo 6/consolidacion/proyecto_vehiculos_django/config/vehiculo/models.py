import datetime

from django.db import models
from django.db.models import Choices


# Create your models here.


class Vehiculo(models.Model):
    marcas_choices = (
        ("Ford", "FORD"),
        ("Fiat", "FIAT"),
        ("Toyota", "TOYOTA"),
        ("Chevrolet", "CHEVROLET")
    )

    categoria_choices = (
        ("Particular", "PARTICULAR"),
        ("Carga", "CARGA"),
        ("Trasporte", "TRANSPORTE"),
    )

    marca = models.CharField(max_length=20, choices=marcas_choices, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.IntegerField()
    categoria = models.CharField(max_length=20, choices=categoria_choices, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now)
    fecha_modificacion = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        permissions = [
            ('visualizar', 'Permiso para visualizar'),
        ]
