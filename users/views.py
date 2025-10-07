from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import datetime

class CreateUser(forms.Form):
    user_name = forms.CharField(label='Names')
    user_role = forms.ChoiceField(choices=[('A', 'Admin'), ('U', 'User')], widget=forms.RadioSelect)

users_list = ["Peter Ngare"]
roles = ["SuperAdmin"]

now = datetime.datetime.now()

def users(request):
    zipped_user_data = zip(users_list, roles)
    return render(request, "users/users.html", {
        "zipped_user_data": zipped_user_data,
        "create_user": CreateUser()
    })

def bonjour(request, name):
    return HttpResponse(f"Bonjour, {name.capitalize()}!")

def is_new_year(request):
    return render(request, "users/index.html", {
        "date": now
    })
