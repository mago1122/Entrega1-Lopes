from django.http import HttpResponse
from appentrega.models import *
from django.shortcuts import render
from django.template import Template, Context

# Create your views here.

def vista_inicio(request):
    return render(request, "appentrega/inicio.html")

def vista_libros(request):
    return render(request, "appentrega/libros.html")

def vista_sucursales(request):
    return render(request, "appentrega/sucursales.html")

def vista_autores(request):
    return render(request, "appentrega/autores.html")

def vista_miembros(request):
    return render(request, "appentrega/miembros.html")