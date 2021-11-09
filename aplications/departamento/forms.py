from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    job = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=50)

    def clean_cantidad(self):
        job = self.cleaned_data.get('job')
        if job == 'Contador' and job == 'Administrador' and job == 'Economista' and job == 'Otros' :
            return job
        raise forms.ValidationError('Ingrese un numero mayor a 10')
