from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.ver, name='contactos'),
    path('crear/', views.crear, name='crear-contacto'),
    path('guardar/', views.guardar, name='guardar-contacto'),
]
