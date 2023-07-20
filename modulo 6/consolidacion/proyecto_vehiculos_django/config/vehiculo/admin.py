from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Vehiculo


# Register your models here.
class VehiculoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
admin.site.site_header = 'Catalogo de Vehiculos'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Panel de Control'
