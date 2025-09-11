from django.shortcuts import render

tasks = [ "sleep", "pray", "eat"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks,
    })

def ask(request, name):
    return render(request, "tasks/ask.html", {
        "name": name.capitalize(),
    })