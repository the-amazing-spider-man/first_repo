from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path("", views.index, name = "patientName"),
    path("medician/",views.medician, name = "medician"),
    path("medical/",views.medical, name = "medical"),
    path("help/",views.help, name = "help"),
]