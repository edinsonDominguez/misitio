from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hora_actual(request):
    ahora = datetime.datetime.now()
    html = " <html><body>It is now %s .</body></html> " % ahora
    
    return HttpResponse(html)

def primera_pagina(request):

    return render(request, 'index.html')