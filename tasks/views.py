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

def add_task(request, tasks, new_task ):
    tasks.append(new_task)
    return render(request, "tasks/add_task.html", )