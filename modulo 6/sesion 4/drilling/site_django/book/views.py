from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.




def index(request): #primera forma(funcion) para views
    return HttpResponse("<h1>Bienvenidos a mi sitio de Libros<h1>")


class IndexPageView(TemplateView):
    template_name = 'index.html'

