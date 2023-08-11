import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import ProductoForm
from .models import Producto


# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'


def listar_productos(request):
    productos = Producto.objects.using('default').all().order_by('precio')
    return render(request, 'lista_productos.html', {'productos': productos})


def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto ingresado exitosamente')
            return redirect('lista_productos')
        else:  # para manejar el error de no cumplir validaciones
            messages.error(request, 'Ingrese datos válidos')
            return HttpResponseRedirect(reverse(add_producto))
    else:
        form = ProductoForm()
        return render(request, 'add.html', {'form': form})


# @login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # producto.fecha_modificacion = datetime.datetime.now()
            messages.success(request, 'producto editado correctamente')
            return redirect('lista_productos')
        else:
            messages.error(request, 'Favor ingresa datos validos')
            return HttpResponseRedirect(reverse('editar_producto', args=[producto_id]))
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'form': form, 'producto_id': producto_id})


# @login_required
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    messages.warning(request, 'producto borrado exitosamente')
    return redirect('lista_productos')
