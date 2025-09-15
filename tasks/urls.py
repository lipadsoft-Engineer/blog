from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="task_index"),
    path("add", views.add_task, name='add_task'),
    path(f"<str:name>", views.ask, name="ask" ),
]