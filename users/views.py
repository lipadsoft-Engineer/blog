from django.http import HttpResponse
from django.shortcuts import render
import datetime

now = datetime.datetime.now()

def users(request):
    return HttpResponse("Hello world!")

def bonjour(request, name):
    return HttpResponse(f"Bonjour, {name.capitalize()}!")

def is_new_year(request):
    return render(request, "users/index.html", {
        "date": now
    })
