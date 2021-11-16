from django.contrib import admin
from django.urls import path

from . import views

app_name = 'departamento_app'

urlpatterns = [
    path(
        'new-departamento/', 
        views.NewDepartamentoView.as_view(), 
        name='new_departamento'
    ),
    path(
        'listado-de-departamentos/', 
        views.DepartamentoListView.as_view(), 
        name='lista_departamento'
    ), 
]
 