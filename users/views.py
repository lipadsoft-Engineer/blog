from django.http import HttpResponse
from django.shortcuts import render
import datetime

users_list = ["Peter Ngare"]
roles = ["SuperAdmin"]

now = datetime.datetime.now()

def users(request):
    zipped_user_data = zip(users_list, roles)
    return render(request, "users/users.html", {
        "zipped_user_data": zipped_user_data,
    })

def bonjour(request, name):
    return HttpResponse(f"Bonjour, {name.capitalize()}!")

def is_new_year(request):
    return render(request, "users/index.html", {
        "date": now
    })
