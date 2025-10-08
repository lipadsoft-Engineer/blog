from django.shortcuts import render
from django.http import HttpResponse

categories = ['Health']
counts = [3]

# Create your views here.
def index(request):
    zipped_blogs_data = zip(categories, counts)
    return render(request, "blogs/index.html", {
        "zipped_blogs_data": zipped_blogs_data
    })

def greet(request, name):
    return render(request, "blogs/greet.html", { "name": name.capitalize() })

