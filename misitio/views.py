from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hora_actual(request):
    ahora = datetime.datetime.now()
    
    return render(request, 'hora.html', {'hora':ahora})

def suma_hora(request, numero):
    numero = int(numero)
    ahora = datetime.datetime.now()
    suma = ahora + datetime.timedelta(hours=numero)

    return render(request, 'hora.html', {'hora_suma':suma})

def nombre_usuario(request, nombre):
    hora = datetime.datetime.now()
        
    return render(request, 'bienvenida.html', {'name_user':nombre, 'hora':hora})

def primera_pagina(request):

    return render(request, 'index.html')

