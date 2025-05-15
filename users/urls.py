from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path("<str:name>", views.bonjour, name="bonjour"),
]
