from django.urls import path

from .views import IndexPageView, lista_libros, crear_libro, editar_libro, borrar_libro, buscar_libro, registro, login, \
    iniciar_sesion, cerrar_sesion, home_page_not_login

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('crear_libro/', crear_libro, name='crear_libro'), 
    path('editar_libro/<int:libro_id>', editar_libro, name='editar_libro'),
    path('borrar_libro/<int:libro_id>', borrar_libro, name='borrar_libro'),
    path('buscar_libro', buscar_libro, name='buscar_libro'),
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('home/', home_page_not_login, name='home')
]