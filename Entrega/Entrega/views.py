from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def vista_index(request):
    return HttpResponse("Hola Martin!")