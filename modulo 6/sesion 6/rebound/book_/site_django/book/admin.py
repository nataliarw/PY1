from django.contrib import admin

from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('id', 'titulo', 'autor', 'valoracion', 'rating')
    list_filter = ('autor', 'valoracion', 'fecha_modificacion')

    @staticmethod
    def rating(obj):
        if obj.valoracion < 1000:
            return 'Baja'
        elif 1000 <= obj.valoracion < 2500:
            return 'Media'
        else:
            return 'Alta'

    rating.short_description = 'Rating'


admin.site.register(Book, BookAdmin)  # registrar modelo libro
