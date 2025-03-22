from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from .models import Producto

# Create your views here.
def registrar_producto(request):
    if request.method == "POST":
        print ('si entro a get ')
        #print(request.POST['nombre'])
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid(): 
            print ('si valido')
            p = Producto()
            p.usuario = request.user
            p.nombre = form.cleaned_data['nombre']
            p.valor = form.cleaned_data['valor']
            p.inventario = form.cleaned_data['inventario']
            p.categoria_producto = form.cleaned_data['categoria']
            p.descripcion = form.cleaned_data['descripcion']
            p.foto1 = form.cleaned_data['foto1']
            p.foto2 = form.cleaned_data['foto2']
            p.foto3 = form.cleaned_data['foto3']
            p.foto4 = form.cleaned_data['foto4']
            p.foto5 = form.cleaned_data['foto5']
            p.foto6 = form.cleaned_data['foto6']
            print(p.nombre, p.valor, p.inventario, p.categoria_producto, p.usuario)
            p.save()           
            ## va la parte del registro de datos
            return redirect('producto/ver_productos') # pagina que se a retornar 
    else:
        form = ProductoForm()
    return render(request, 'producto/registro_productos.html', {'form':form})    


def ver_producto(request):
    nombre_buscar = request.GET.get('q', '')
       
    if nombre_buscar:
        print('nombre: ', nombre_buscar)
        mi_producto = Producto.objects.filter(nombre=nombre_buscar, usuario=request.user, estado=True)
    else:
        print('no hay que mostrar')
        #miProducto = Producto.objects.all() 
        mi_producto = Producto.objects.filter(usuario=request.user, estado=True)

        #return render(request, 'productos.html', {'producto': miProducto, 'nombre': nombre_buscar})
    return render(request, 'producto/productos_registrados.html', {'producto':mi_producto, 'nombre': nombre_buscar})

def ver_inicio(request):
    return render(request, 'producto/inicio.html')


def galeria_usuario(request):
    nombre_buscar = request.GET.get('q', '')
       
    if nombre_buscar:
        print('nombre: ', nombre_buscar)
        mis_fotos = Producto.objects.filter(usuario=request.user, nombre=nombre_buscar, estado=True)
    else:
        print('no hay que mostrar')
        mis_fotos = Producto.objects.filter(usuario=request.user, estado=True)
 
    return render(request, 'producto/galeria_fotos.html', {'galeria': mis_fotos, 'nombre': nombre_buscar})

# se muestra la informacion del producto que seleccionamos 
def producto_usuario(request, producto_id):
    mi_producto = Producto.objects.get(id=producto_id)
    return render(request, 'producto/info_producto_usuario.html', {'producto': mi_producto})

# edita los campos de los productos
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    form = ProductoForm(initial ={
        'nombre': producto.nombre,
        'valor': producto.valor,
        'inventario': producto.inventario,
        'categoria': producto.categoria_producto,
        'foto1': producto.foto1,
        'foto2': producto.foto2,
        'foto3': producto.foto3,
        'foto4': producto.foto4,
        'foto5': producto.foto5,
        'foto6': producto.foto6,
        })
    
    if request.method == "POST":
        print ('si entro a get ')
        #print(request.POST['nombre'])
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid(): 
            print ('si valido')
            
            producto.usuario = request.user
            producto.nombre = form.cleaned_data['nombre']
            producto.valor = form.cleaned_data['valor']
            producto.inventario = form.cleaned_data['inventario']
            producto.categoria_producto = form.cleaned_data['categoria']
            producto.foto1 = form.cleaned_data['foto1']
            producto.foto2 = form.cleaned_data['foto2']
            producto.foto3 = form.cleaned_data['foto3']
            producto.foto4 = form.cleaned_data['foto4']
            producto.foto5 = form.cleaned_data['foto5']
            producto.foto6 = form.cleaned_data['foto6']
            #print(p.nombre, p.valor, p.inventario, p.categoria_producto, p.usuario)
            producto.save()           
            ## va la parte del registro de datos
            return redirect('producto/ver_productos') # pagina que se a retornar 
    else:
        print('no hay nada')
    
    return render(request, 'producto/editar_producto.html', {'form':form})

# elimina el producto de la vista usuario
def eliminar_producto(request, producto_id):
    print('se elimino el id', producto_id)
    Producto.objects.filter(id=producto_id).update(estado=False)
    return render(request, 'producto/mensaje_eliminar.html')
