from django.shortcuts import render, redirect, get_object_or_404
from producto.models import Producto, Categoria
from .forms import FormContacto
from comentarios.forms import ComentarioForm
from comentarios.models import Comentarios 

# Create your views here.
def ver_inicio(request):
    return render(request, 'home.html')

def ver_productos(request):
    
    ## lista de las categorias que van a ir en el nav
    categoria = Categoria.objects.all()
    mi_producto=Producto.objects.filter(estado=True)[:12]
      
    return render(request, 'productos.html', {'producto': mi_producto, 'categoria':categoria})

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

# se toma el comentario del usuario 
def agregar_comentario(request, pk):
    producto = get_object_or_404(Producto, id = pk)
    mensaje = request.GET.get('q')
 
    c = Comentarios()
    c.id_usuario = request.user
    c.id_producto = producto
    c.comentario = mensaje
    c.save()

    return redirect('mensaje_correo')

# se va a mostrar la informacion del producto que selecionamos
def info_producto(request, producto_id):
    mi_producto = Producto.objects.get(id=producto_id)
    
    
    return render(request, 'informacion_producto.html', {'producto': mi_producto})

# se van a mostrar los productos que estan en la categoria
def info_categoria(request, pk):
    categoria = Categoria.objects.all()
    producto = Producto.objects.filter(categoria_producto=pk, estado=True)[:12]
    return render(request, 'productos.html', {'producto':producto, 'categoria':categoria}  )


# se van a organizar los productos de mayor a menor y viceversa
def info_precio(request):
    categoria = Categoria.objects.all()
    mensaje = request.GET.get('q')
    print('el valor del mensaje: ', mensaje)

    if mensaje == 'mayor':
        productos = Producto.objects.filter(estado=True).order_by('-valor')[:12]
    if mensaje == 'menor':
        productos = Producto.objects.filter(estado=True).order_by('valor')[:12]
        
    return render(request, 'productos.html', {'producto':productos, 'categoria': categoria} )

# busca los productos por el nombre
def buscador(request):
    categoria = Categoria.objects.all()
    mi_producto = Producto.objects.filter(estado=True)[:12]
    
    nombre_buscar = request.GET.get('q')
    print('nombre: ', nombre_buscar)

    if nombre_buscar:
        mi_producto = Producto.objects.filter(nombre__icontains=nombre_buscar, estado=True)
    else:
        mi_producto = Producto.objects.filter(estado=True)[:12] 
  
    return render(request, 'productos.html', {'producto':mi_producto, 'categoria':categoria} )
