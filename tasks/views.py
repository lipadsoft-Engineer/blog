from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


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

def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/add_task.html", {
                "form":form
            })

    return render(request, "tasks/add_task.html", {
        "form": NewTaskForm()
    } )