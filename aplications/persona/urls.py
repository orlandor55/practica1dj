from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('lista-colaboradores/', views.ListColaboradores.as_view()),
    path('lista-colaboradores-por-area/<short_name>/', views.ListarPorArea.as_view()),
]
