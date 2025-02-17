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
        """
        esta es la logica correspondiente al envio del correo electronico
            nombre = request.POST.get('nombre')
            correo = request.POST.get('email')
            mensaje = request.POST.get('contenido')
            
            email = EmailMessage('Mensaje del asunto: ', 
                         'nombre de usuario: {} \n correo: {} \n\n mensaje: {}'.format(nombre, correo, mensaje),
                         '', ['correo@gmail.com'], reply_to=[correo])

            adicional hay que agregar una variables en settings

        """

        return redirect('mensaje_correo')
    
    return render(request, 'contacto.html', {'miform':miform})

# mensaje exitoso de envio del correo
def ver_mensaje_correo(request):

    return render(request, 'mensaje_correo.html')

# informacion de la empresa 
def ver_informacion(request):
    return render(request, 'informacion.html')

