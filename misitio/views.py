from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hora_actual(request):
    ahora = datetime.datetime.now()
    
    return render(request, 'hora.html', {'hora':ahora})

def suma_hora(request, numero):
    # debemos cambiar este metodo tambien 
    print (numero)
    numero = int(numero)
    ahora = datetime.datetime.now()
    suma = ahora + datetime.timedelta(hours=numero)
    html = " <html><body>In %s hour(s), it will be %s .</body></html> " % (numero, suma)
    
    return HttpResponse(html)

def primera_pagina(request):

    return render(request, 'index.html')