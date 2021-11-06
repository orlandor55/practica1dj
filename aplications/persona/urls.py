from django.contrib import admin
from django.urls import path

from . import views


app_name = 'persona_app'

urlpatterns = [
    path('lista-colaboradores/', views.ListColaboradores.as_view()),
    path('lista-colaboradores-por-area/<short_name>/', views.ListarPorArea.as_view()),
    path('buscar-colaborador/', views.ListarPorKW.as_view()),
    path('habilidades-colaborador/', views.ListarHabilidades.as_view()),
    path('lista-colaboradores-por-cargo/<cargo>/', views.ListarPorCargo.as_view()),
    path('detalle-colaborador/<pk>', views.ColaboradorDetailView.as_view()),
    path('add-colaborador/', views.ColaboradorCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='registro_correcto'),
    path('actualizar-colaborador/<pk>', views.ColaboradorUpdateView.as_view(), name='actualizar'),
    path('update-success/', views.UpdateSuccessView.as_view(), name='actualizacion-exitosa'),
    path('eliminar-colaborador/<pk>', views.ColaboradorDeleteView.as_view(), name='eliminar'),

]
 