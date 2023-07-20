from django.urls import path

from .views import IndexPageView, lista_vehiculos, add_vehiculo, registro, iniciar_sesion, cerrar_sesion, \
    home_page_not_login

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('lista_vehiculos/', lista_vehiculos, name='lista_vehiculos'),
    path('add/', add_vehiculo, name='add'),
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('home/', home_page_not_login, name='home'),

]