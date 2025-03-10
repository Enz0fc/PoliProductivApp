from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_semestres/', views.get_semestres, name='get_semestres'),
    path('get_materias/', views.get_materias, name='get_materias'),
    path('get_secciones/', views.get_secciones, name='get_secciones'),
]