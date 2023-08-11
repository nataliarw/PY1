import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentTypefrom, ContentType
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from .form import BookForm
from .models import Book


# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'


@login_required
def lista_libros(request):
    libros = Book.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})


# view o controlador para crear libros
@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nuevo libro ingresado exitosamente')
            return redirect('lista_libros')
        else:  # para manejar el error de no cumplir validaciones
            messages.error(request, 'Ingrese datos válidos')
            return HttpResponseRedirect(reverse(crear_libro))
    else:
        form = BookForm()
        return render(request, 'crear_libro.html', {'form': form})


@login_required
def editar_libro(request, libro_id):
    book = get_object_or_404(Book, id=libro_id)  # obtener un libro por id
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.fecha_modificacion = datetime.datetime.now()
            messages.success(request, 'libro editado correctamente')
            return redirect('lista_libros')
        else:
            messages.error(request, 'Favor ingresa datos validos')
            return HttpResponseRedirect(reverse('editar_libro', args=[libro_id]))
    else:
        form = BookForm(instance=book)
        return render(request, 'editar_libro.html', {'form': form, 'libro_id': libro_id})


@login_required
def borrar_libro(request, libro_id):
    book = get_object_or_404(Book, id=libro_id)
    book.delete()
    messages.warning(request, 'Libro borrado exitosamente')
    return redirect('lista_libros')


@login_required
def buscar_libro(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        libros = Book.objects.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
        return render(request, 'buscar_libro.html', {'libros': libros})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            content_type = ContentType.objects.get_for_model(Book)
            permission = Permission.objects.get(
                codename="development",
                content_type=content_type,
            )
            user.user_permissions.add(permission)
            messages.success(request, 'Registrado exitosamente')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


# view o controlador para el iniciar sesion

def iniciar_sesion(request):
    if request.method == 'POST':  # si el request es de tipo post
        username = request.POST['username']  # captura username del request
        password = request.POST['password']  # captura password del request
        user = authenticate(request, username=username, password=password)  # se captura el usuario encontrado
        if user is not None:  # si el usuario autenticado no viene vacio, quiere decir es validas sus credenciales
            login(request, user)
            return redirect('lista_libros')
        else:
            messages.error(request, 'Usuario o password inválidas')
            return render(request, 'login.html')
    return render(request, 'login.html')  # tipo get


# view o controlador para cerrar sesion
def cerrar_sesion(request):
    logout(request)  # se deslogue
    return render(request, 'login.html')


def home_page_not_login(request):
    return render(request, 'index.html')
