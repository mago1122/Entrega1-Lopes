from django.http import HttpResponse

def vista_index(request):
    return HttpResponse("Hola Martin!")