import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from .form import LaboratorioForm
from .models import Laboratorio



class IndexPageView(TemplateView):
    template_name = 'index.html'

# Create your views here.
def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'lista_laboratorios.html', {'laboratorios': laboratorios})

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nuevo laboratorio creado exitosamente')
            return redirect('lista_laboratorios')
        else:  # para manejar el error de no cumplir validaciones
            messages.error(request, 'Ingrese datos válidos')
            return HttpResponseRedirect(reverse(crear_laboratorio))
    else:
        form = LaboratorioForm()
        return render(request, 'crear_laboratorio.html', {'form': form})


# @login_required
def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)  # obtener un laboratorio por id
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            messages.success(request, 'laboratorio editado correctamente')
            return redirect('lista_laboratorios')
        else:
            messages.error(request, 'Favor ingresa datos validos')
            return HttpResponseRedirect(reverse('editar_laboratorio', args=[laboratorio_id]))
    else:
        form = LaboratorioForm(instance=laboratorio)
        return render(request, 'editar_laboratorio.html', {'form': form, 'laboratorio_id': laboratorio_id})


# @login_required
def borrar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    laboratorio.delete()
    messages.warning(request, 'Laboratorio borrado exitosamente')
    return redirect('lista_laboratorios')