from django.db import models


# Create your models here.
class Fabrica(models.Model):
    nombre = models.CharField(max_length=10)
    pais = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=60)
    f_vencimiento = models.DateField(blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)

