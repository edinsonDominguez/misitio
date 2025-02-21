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
        miProducto = Producto.objects.filter(nombre=nombre_buscar, estado=True)
    else:
        print('no hay que mostrar')
        miProducto = Producto.objects.all() 
        
    return render(request, 'productos.html', {'producto': miProducto, 'nombre': nombre_buscar})

def ver_contacto(request):

    if request.method == "POST":
        print ('si entro formulario !!')
        mi_form = FormContacto(request.POST)

        if mi_form.is_valid():
            return redirect('mensaje_correo')
    
    else:
        mi_form = FormContacto()
    return render(request, 'contacto.html', {'form':mi_form})

# mensaje exitoso de envio del correo
def ver_mensaje_correo(request):

    return render(request, 'mensaje_correo.html')

# informacion de la empresa 
def ver_informacion(request):
    return render(request, 'informacion.html')

# se va a mostrar la informacion del producto que selecionamos
def info_producto(request, producto_id):
    mi_producto = Producto.objects.get(id=producto_id)

    return render(request, 'informacion_producto.html', {'producto': mi_producto})

