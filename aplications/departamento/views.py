from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm
from .models import Departamento
from aplications.persona.models import Colaborador

# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self,form):
        print('Estamos en form valid')
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['short_name']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        job = ['job']
        Colaborador.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = job,
            departamento = depa
        )

        return super(NewDepartamentoView, self).form_valid(form)

