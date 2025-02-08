from django.shortcuts import render, redirect
from .forms import ProductoForm, AlbumForm
from .models import Imagen, Producto
from django.contrib.auth.models import User

# Create your views here.

def get_album(request):
    # esta en espera este codigo
    if request.method == "POST":
        print ('si entro a get_album ')
        form = AlbumForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            print ('si valido los registros')
            ## va la parte del registro de datos
            return redirect('ver_albumnes') # pagina que se a retornar 
    else:
        form = AlbumForm()
    return render(request, 'registro_imagen.html', {'form':form})  

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
            p.foto1 = form.cleaned_data['foto1']
            p.foto2 = form.cleaned_data['foto2']
            p.foto3 = form.cleaned_data['foto3']
            p.foto4 = form.cleaned_data['foto4']
            p.foto5 = form.cleaned_data['foto5']
            p.foto6 = form.cleaned_data['foto6']
            print(p.nombre, p.valor, p.inventario, p.categoria_producto, p.usuario)
            p.save()           
            ## va la parte del registro de datos
            return redirect('ver_productos') # pagina que se a retornar 
    else:
        form = ProductoForm()
    return render(request, 'registro_alcobas.html', {'form':form})    


def ver_alcoba(request):
    return render(request, 'alcobas.html')


def ver_producto(request):
    return render(request, 'productos_registrados.html')

def ver_album(request):
    return render(request, 'albumnes_registrados.html')

def ver_inicio(request):
    return render(request, 'inicio.html')

#def registrar_alcobas(request):
 #   return render(request, 'registro_alcobas.html')
