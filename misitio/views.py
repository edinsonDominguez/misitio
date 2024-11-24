from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hora_actual(request):
    ahora = datetime.datetime.now()
    html = " <html><body>It is now %s .</body></html> " % ahora
    
    return HttpResponse(html)

def suma_hora(request, numero):
    print (numero)
    numero = int(numero)
    ahora = datetime.datetime.now()
    suma = ahora + datetime.timedelta(hours=numero)
    html = " <html><body>In %s hour(s), it will be %s .</body></html> " % (numero, suma)
    
    return HttpResponse(html)

def primera_pagina(request):

    return render(request, 'index.html')