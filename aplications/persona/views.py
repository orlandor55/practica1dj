from django.shortcuts import render

from django.views.generic import (
    ListView, 
)

from .models import Colaborador
# Create your views here.


class ListColaboradores(ListView):
    template_name = 'persona/list_all.html'
    model = Colaborador
    context_object_name = 'lista_colaboradores'



class ListarPorArea(ListView):
    model = Colaborador
    template_name = "persona/list_por_area.html"
    context_object_name = 'lista_por_area'
    # queryset = Colaborador.objects.filter(
    #     departamento__short_name = 'AAS'
    # )

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Colaborador.objects.filter(
        departamento__short_name=area
        )

        return lista
    