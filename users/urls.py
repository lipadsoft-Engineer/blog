from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path("new year/", views.is_new_year, name="new_year"),
    path("profile/", views.profile, name="profile"),
    path(f"<str:name>/", views.bonjour, name="bonjour"),
]
