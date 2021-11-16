from django import forms

from .models import Colaborador

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = (
        'first_name', 
        'last_name', 
        'job', 
        'departamento', 
        'foto',
        'habilidad'
    )
        widgets = {
            'habilidad': forms.CheckboxSelectMultiple()
        }