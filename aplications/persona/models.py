from django.db import models
from aplications.departamento.models import Departamento
# Create your models here.
class Colaborador(models.Model):

    JOB_CHOICE = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otros'),
    )

    first_name = models.CharField('Nombre', max_length=15)
    last_name = models.CharField('Nombre', max_length=15)
    job = models.CharField('Cargo', max_length=50, choices=JOB_CHOICE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #foto = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.first_name + " " + self.last_name
