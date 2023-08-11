from django.contrib import admin

from .models import Fabrica, Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'costo', 'f_vencimiento', 'fabrica')
    list_filter = ('nombre', 'fabrica')
    list_per_page = 3
    # list_editable = ['descripcion']
    ordering = ['precio']
    search_fields = ['nombre']

    def costo(self, obj):
        if obj.precio >=2500:
            return 'Costo Alto'
        else:
            return 'Costo Bajo'


class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')


# Register your models here.
admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.site_header = 'Catalogo de Productos'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Panel de Control'
