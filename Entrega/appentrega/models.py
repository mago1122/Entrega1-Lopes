from django.db import models

# Create your models here.

class Libros(models.Model):

    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    precio = models.IntegerField()

class Sucursales(models.Model):

    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()

class Autores(models.Model):

    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    año_nacimiento = models.DateField()

class Miembros(models.Model):

    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    email = models.EmailField()
