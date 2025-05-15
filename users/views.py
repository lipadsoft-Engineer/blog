from django.http import HttpResponse

def users(request):
    return HttpResponse("Hello world!")

def bonjour(request):
    return HttpResponse("Bonjour, peter")
