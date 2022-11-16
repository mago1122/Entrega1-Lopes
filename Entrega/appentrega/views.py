from django.http import HttpResponse
from appentrega.models import *
from django.shortcuts import render
from django.template import Template, Context

# Create your views here.

def vista_inicio(request):
    return render(request, "appentrega/inicio.html")


def vista_libros(request):

    if request.method == "POST":

        titulo_libro = request.POST["titulo"]
        autor_libro = request.POST["autor"]
        precio_libro = request.POST["precio"]
    
        libro = Libros(titulo=titulo_libro, autor=autor_libro, precio=precio_libro)
        libro.save()

    return render(request, "appentrega/libros.html")


def vista_sucursales(request):

    if request.method == "POST":

        nombre_sucursal = request.POST["nombre"]
        nombre_calle = request.POST["calle"]
        numero_calle = request.POST["numero"]
    
        sucursal = Sucursales(nombre=nombre_sucursal, calle=nombre_calle, numero=numero_calle)
        sucursal.save()

    return render(request, "appentrega/sucursales.html")


def vista_autores(request):

    if request.method == "POST":

        nombre_autor= request.POST["nombre"]
        apellido_autor = request.POST["apellido"]
        nacimiento = request.POST["año_nacimiento"]
    
        autor = Autores(nombre=nombre_autor, apellido=apellido_autor, año_nacimiento=nacimiento)
        autor.save()

    return render(request, "appentrega/autores.html")


def vista_miembros(request):

    if request.method == "POST":

        nombre_miembro= request.POST["nombre"]
        apellido_miembro = request.POST["apellido"]
        email_miembro = request.POST["email"]
    
        miembro = Miembros(nombre=nombre_miembro, apellido=apellido_miembro, email=email_miembro)
        miembro.save()


    return render(request, "appentrega/miembros.html")