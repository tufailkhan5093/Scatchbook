from django.urls import path
from . import views

urlpatterns = [
    path("", views.visit, name="visit"),
    path("add/", views.add, name="add"),
    path("done/", views.done, name="done"),
]
