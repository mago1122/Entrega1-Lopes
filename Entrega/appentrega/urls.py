from django.urls import path
from appentrega.views import *

urlpatterns = [

    path("libros/", vista_libros),
    path("sucursales/", vista_sucursales),
    path("autores/", vista_autores),
    path("miembros/", vista_miembros),
    path("inicio/", vista_inicio),
    path("buscar/", buscar_libro),
    path("resultados/", resultado_buscar_libro)

]