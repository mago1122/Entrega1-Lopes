from django.http import HttpResponse
from appentrega.models import *
from django.shortcuts import render
from django.template import Template, Context

# Create your views here.

def vista_inicio(request):

    return render(request, "appentrega/inicio.html")


def vista_libros(request):
    return HttpResponse("Estas en la vista: formulario de libros")

def vista_sucursales(request):
    return HttpResponse("Estas en la vista: formulario de sucursales")

def vista_autores(request):
    return HttpResponse("Estas en la vista: formulario de autores")

def vista_miembros(request):
    return HttpResponse("Estas en la vista: formulario de miembros")