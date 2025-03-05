from django.shortcuts import render, redirect
from .logica import Compra
from producto.models import Producto
# Create your views here.

# se visualizaran los productos que ingresamos al carrito de compras

#def ver_carro(request):
#    return render(request, 'carro_compra.html')

# va agregar el producto al carrito
def agregar_producto(request, producto_id):
    compra = Compra(request)
    producto = Producto.objects.get(id=producto_id)

    # le enviamos el producto que recuperamos con el id
    compra.agregar(producto=producto)

    return redirect('Productos')

def eliminar_producto(request, producto_id):

    compra = Compra(request)
    producto = Producto.objects.get(id=producto_id)
    compra.eliminar(producto=producto)

    return redirect('Productos')

def restar_producto(request, producto_id):
    compra = Compra(request)
    producto=Producto.objects.get(id=producto_id)

    compra.restar_producto(producto=producto)
    return redirect('Productos')

def limpiar_compra(request):
    compra = Compra(request)
    compra.limpiar_compra()

    return redirect('Productos')