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
    paginate_by = 2



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


class ListarPorKW(ListView):
    template_name = "persona/list_por_kw.html"
    context_object_name = 'lista_por_kw'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Colaborador.objects.filter(
            first_name = palabra_clave
        )

        return lista



class ListarHabilidades(ListView):
    template_name = "persona/habilidades_colaborador.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        habilidades = Colaborador.objects.get(id=4)
        print(habilidades.habilidad.all())
        
        return [habilidades]


class ListarPorCargo(ListView):
    template_name = "persona/list_por_trabajo.html"
    context_object_name = 'lista_por_cargo'
    # queryset = Colaborador.objects.filter(
    #     job = '0'
    # )

    def get_queryset(self):
        cargo = self.kwargs['cargo']
        lista = Colaborador.objects.filter(
            job=cargo
            )
            
        # cargo = self.request.GET.get('job','')
        # lista = Colaborador.objects.filter(
        #     job = cargo
        # )

        return lista
