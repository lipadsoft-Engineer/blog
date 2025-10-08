from django.shortcuts import render
from django import forms
from django.http import HttpResponse


class NewBlogForm(forms.Form):
    category = forms.CharField(label='Category')
    count = forms.IntegerField(label='Count', min_value=2, max_value=20)

categories = ['Health']
counts = [3]

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NewBlogForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category'].capitalize()
            categories.append(category)
            count = form.cleaned_data['count']
            counts.append(count)
        else:
            return render(request, "blogs/index.html", {
                "form": NewBlogForm(form)
            })

    zipped_blogs_data = zip(categories, counts)
    return render(request, "blogs/index.html", {
        "zipped_blogs_data": zipped_blogs_data,
        "form": NewBlogForm()
    })

def greet(request, name):
    return render(request, "blogs/greet.html", { "name": name.capitalize() })

