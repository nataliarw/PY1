from django.urls import path

from .views import listar_productos, add_producto, IndexPageView, editar_producto, borrar_producto

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('lista_productos/', listar_productos, name='lista_productos'),
    path('add/', add_producto, name='add'),
    path('editar_producto/<int:producto_id>', editar_producto, name='editar_producto'),
    path('borrar_producto/<int:producto_id>', borrar_producto, name='borrar_producto'),
    # path('registro/', registro, name='registro'),
    # path('login/', iniciar_sesion, name='login'),
    # path('logout/', cerrar_sesion, name='logout'),
    # path('home/', home_page_not_login, name='home'),

]