from django.contrib import admin
from django.urls import path

def Desdeapp(self):
    print('================================ Saludos desde App Departamento=========================')

urlpatterns = [
    path('departamento/', Desdeapp),
]
