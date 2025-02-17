from django.shortcuts import render, redirect
from producto.models import Producto
from .forms import FormContacto

# Create your views here.
def ver_inicio(request):
    return render(request, 'home.html')

def ver_productos(request):
    
    nombre_buscar = request.GET.get('q', '')
       
        
    if nombre_buscar:
        print('nombre: ', nombre_buscar)
        miProducto = Producto.objects.filter(nombre=nombre_buscar)
    else:
        print('no hay que mostrar')
        miProducto = Producto.objects.all() 
        
    return render(request, 'productos.html', {'producto': miProducto, 'nombre': nombre_buscar})

def ver_contacto(request):

    miform = FormContacto(request.POST)

    if miform.is_valid():
        print('si valido')
        return redirect('mensaje_correo')
    
    return render(request, 'contacto.html', {'miform':miform})

# mensaje exitoso del correo

def ver_mensaje_correo(request):

    return render(request, 'mensaje_correo.html')

# informacion de la empresa 
def ver_informacion(request):
    return render(request, 'informacion.html')

