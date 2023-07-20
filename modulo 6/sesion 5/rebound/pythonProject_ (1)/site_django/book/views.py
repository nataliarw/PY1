from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def index(request):  # forma para establecer un views o controlador mediante una funcion
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")


class IndexPageView(TemplateView):  # forma d utilizar una clase heredando desd TemplateView para renderizar un template
    template_name = 'index.html'

    #sesion 5 metodo para agregar
def palindromo(request, palabra):
    print(palabra) #para probar
    es_palidromo =""
    #reemplazamos espacios de la palabra por elementos vacios
    palabra_sin_espacio = palabra.replace(" ", "")
    if palabra_sin_espacio == palabra_sin_espacio[::-1]:
        es_palindromo = "ES PALINDROMO"
    else:
        es_palindromo = "NO ES PALINDROMO"
    #SETEAR DATOS EN EL CONTEXT QUE VIAJA EN EL RESPONSE
    context = {'es_palindromo': es_palindromo, 'palabra': palabra}
    #retornamos a un template
    return render(request, 'espalindromo.html', context)



