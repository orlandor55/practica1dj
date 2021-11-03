from django.contrib import admin
from django.urls import path

def Desdeapp(self):
    print('================================ Saludos desde App Persona=========================')

urlpatterns = [
    path('persona/', Desdeapp),
]
