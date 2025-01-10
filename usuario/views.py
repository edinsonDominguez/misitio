from django.shortcuts import render

# Create your views here.

def ver_alcoba(request):
    return render(request, 'alcobas.html')


def registrar_alcobas(request):
    return render(request, 'registro_alcobas.html')


