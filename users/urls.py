from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path("<str:name>", views.bonjour, name="bonjour"),
    path("new year/", views.is_new_year, name="new_year")
]
