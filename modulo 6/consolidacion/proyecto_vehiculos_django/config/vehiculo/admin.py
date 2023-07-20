from django.contrib import admin

from .models import Vehiculo


# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'precio', 'condicion_precio')
    list_filter = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'precio')

    @staticmethod
    def condicion_precio(obj):
        if obj.precio < 10000:
            return 'Baja'
        elif 10000 <= obj.precio < 30000:
            return 'Media'
        else:
            return 'Alta'

    condicion_precio.short_description = 'Condicion_de_Precio'


admin.site.register(Vehiculo, VehiculoAdmin)
