import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import VehiculoForm, CustomUserCreationForm
from .models import Vehiculo
from django.db import models


# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'



def condicion_precio(obj):
    if obj.precio < 10000:
        obj.condicion_precio = 'Baja'
    elif 10000 <= obj.precio < 30000:
        obj.condicion_precio = 'Media'
    else:
        obj.condicion_precio = 'Alta'
    return obj


def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    vehiculos_con_condicion = []
    for v in vehiculos:
        v = condicion_precio(v)
        vehiculos_con_condicion.append(v)

    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos_con_condicion})




# view o controlador para crear libros
@permission_required("vehiculo.add_vehiculo")
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo ingresado exitosamente')
            return redirect('lista_vehiculos')
        else:  # para manejar el error de no cumplir validaciones
            messages.error(request, 'Ingrese datos válidos')
            return HttpResponseRedirect(reverse(add_vehiculo))
    else:
        form = VehiculoForm()
        return render(request, 'add.html', {'form': form})




def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permission = Permission.objects.get(
                codename="visualizar",
                content_type=content_type,
            )
            user.user_permissions.add(permission)
            messages.success(request, 'Registrado exitosamente')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


# view o controlador para el iniciar sesion

def iniciar_sesion(request):
    if request.method == 'POST':  # si el request es de tipo post
        username = request.POST['username']  # captura username del request
        password = request.POST['password']  # captura password del request
        user = authenticate(request, username=username, password=password)  # se captura el usuario encontrado
        if user is not None:  # si el usuario autenticado no viene vacio, quiere decir es validas sus credenciales
            login(request, user)
            return redirect('lista_vehiculos')
        else:
            messages.error(request, 'Usuario o password inválidas')
            return render(request, 'login.html')
    return render(request, 'login.html')  # tipo get


# view o controlador para cerrar sesion
@login_required
def cerrar_sesion(request):
    logout(request)  # se deslogue
    return render(request, 'login.html')


def home_page_not_login(request):
    return render(request, 'index.html')
