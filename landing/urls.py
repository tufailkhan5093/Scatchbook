from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="landing_page"),
    path("FAQ/", views.faq, name="faq"),
]
