from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
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
        habilidades = self.request.GET.get('hbd','')
        print('===================', habilidades)
        if habilidades == '':
            return[]
        else:
            colaborador = Colaborador.objects.get(id=habilidades)
            print('===================>', colaborador)
            print('===================>>', colaborador.habilidad.all())
            return colaborador.habilidad.all()


class ListarPorCargo(ListView):
    template_name = "persona/list_por_trabajo.html"
    context_object_name = 'lista_por_cargo'

    def get_queryset(self):
        cargo = self.kwargs['cargo']
        lista = Colaborador.objects.filter(
            job=cargo
            )

        return lista



class ColaboradorDetailView(DetailView):
    model = Colaborador
    template_name = "persona/detalle_colaborador.html"
 
    def get_context_data(self, **kwargs):
        context = super(ColaboradorDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Colaborador del mes'
        print('============',context)
        return context
    


class SuccessView(TemplateView):
    template_name = "persona/success.html"



class ColaboradorCreateView(CreateView):
    model = Colaborador
    template_name = "persona/add.html"
    fields = fields = [
        'first_name', 
        'last_name', 
        'job', 
        'departamento', 
        'habilidad'
    ]
    success_url = reverse_lazy('persona_app:registro_correcto')

    def form_valid(self, form):
        colaborador = form.save(commit=False) #Sirve para evitar guardar varias veces
        colaborador.full_name = colaborador.first_name + ' ' + colaborador.last_name
        colaborador.save()
        return super(ColaboradorCreateView, self).form_valid(form)


class UpdateSuccessView(TemplateView):
    template_name = "persona/update_success.html"


class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    template_name = "persona/update.html"
    fields = [
        'first_name', 
        'last_name', 
        'job', 
        'departamento', 
        'habilidad'
    ]
    success_url = reverse_lazy('persona_app:actualizacion-exitosa')



class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:actualizacion-exitosa')
