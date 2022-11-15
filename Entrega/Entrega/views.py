from django.http import HttpResponse
from datetime import datetime

def vista_index(request):
    return HttpResponse("Hola Martin!")