from datetime import date

from django.core.validators import MinValueValidator
from django.db import models


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=30, blank=True)
    pais = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=30, blank=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators= [MinValueValidator(limit_value=date(2015, 1, 1))])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

