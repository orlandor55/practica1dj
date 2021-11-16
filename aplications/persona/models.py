from ckeditor.fields import RichTextField
#
from django.db import models
#
from aplications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidades del Colaborador', max_length=50)

    class Meta:
        """Meta definition for Habilidades."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.habilidad


class Colaborador(models.Model):

    JOB_CHOICE = (
        ('contador', 'Contador'),
        ('administrador', 'Administrador'),
        ('economista', 'Economista'),
        ('otros', 'Otros'),
    )

    first_name = models.CharField('Nombre', max_length=15)
    last_name = models.CharField('Apellido', max_length=15)
    full_name  = models.CharField('Nombre Completo', max_length=30, blank=True)
    job = models.CharField('Cargo', max_length=50, choices=JOB_CHOICE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='colaborador', blank=True, null=True)
    habilidad = models.ManyToManyField(Habilidades)
    bio = RichTextField()

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return self.first_name + " " + self.last_name
