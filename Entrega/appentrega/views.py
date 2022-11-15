from django.http import HttpResponse
from appentrega.models import *
from django.shortcuts import render

# Create your views here.

def vista_inicio(request):
    return HttpResponse("Estas en el inicio")

def vista_libros(request):
    return HttpResponse("Estas en la vista: formulario de libros")

def vista_sucursales(request):
    return HttpResponse("Estas en la vista: formulario de sucursales")

def vista_autores(request):
    return HttpResponse("Estas en la vista: formulario de autores")

def vista_miembros(request):
    return HttpResponse("Estas en la vista: formulario de miembros")