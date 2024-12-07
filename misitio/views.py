from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .logica import Tarea
from .persona import Persona

mi_tarea = Tarea()

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


def persona(request):
    p = Persona    

    return render(request, 'persona.html', {'persona': p('edinson', 'dominguez', '12')})

def persona_sistema(request):
    p2 = mi_tarea.registrarPersona

    return render(request, 'persona_sistem.html', {'persona2': p2})