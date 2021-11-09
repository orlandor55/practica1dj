from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)

from .models import Prueba

from .forms import PruebaForm


class HomeView(TemplateView):
    template_name = 'home/index.html'



class PruebaListView(ListView):
    #model = Prueba
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = [1,2,3,4,5,6]


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'listaPrueba'



class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'