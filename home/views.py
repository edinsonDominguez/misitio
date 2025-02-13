from django.shortcuts import render

# Create your views here.
def ver_inicio(request):
    return render(request, 'home.html')

def ver_productos(request):
    return render(request, 'productos.html')

def ver_contacto(request):
    return render(request, 'contacto.html')

# informacion de la empresa 
def ver_informacion(request):
    return render(request, 'informacion.html')

