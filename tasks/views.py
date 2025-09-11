from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "tasks/index.html")

def ask(request, name):
    return render(request, "tasks/ask.html", {
        "name": name.capitalize(),
    })