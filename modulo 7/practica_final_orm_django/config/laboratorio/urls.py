from django.urls import path

from .views import listar_laboratorios, crear_laboratorio, editar_laboratorio, borrar_laboratorio, IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('lista_laboratorios/', listar_laboratorios, name='lista_laboratorios'),
    path('crear_laboratorio/', crear_laboratorio, name='crear_laboratorio'),
    path('editar_laboratorio/<int:laboratorio_id>', editar_laboratorio, name='editar_laboratorio'),
    path('borrar_laboratorio/<int:laboratorio_id>', borrar_laboratorio, name='borrar_laboratorio'),



]