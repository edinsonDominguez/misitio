from django.shortcuts import render, redirect
from .forms import ProductoForm, AlbumForm
from .models import Imagen, Producto

# Create your views here.
def get_album(request):
    if request.method == "POST":
        print ('si entro a get_album ')
        form = AlbumForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            print ('si valido los registros')
            ## va la parte del registro de datos
            return redirect('Alcoba') # pagina que se a retornar 
    else:
        form = AlbumForm()
    return render(request, 'registro_imagen.html', {'form':form})  

def registrar_producto(request):
    if request.method == "POST":
        print ('si entro a get ')
        #print(request.POST['nombre'])
        form = ProductoForm(request.POST)
        if form.is_valid(): 
            print ('si valido')
            p = Producto()
            
        
            ## va la parte del registro de datos
            return redirect('ver_lista') # pagina que se a retornar 
    else:
        form = ProductoForm()
    return render(request, 'registro_alcobas.html', {'form':form})    


def ver_alcoba(request):
    return render(request, 'alcobas.html')


def ver_registro(request):
    return render(request, 'productos_registrados.html')

def ver_inicio(request):
    return render(request, 'inicio.html')

#def registrar_alcobas(request):
 #   return render(request, 'registro_alcobas.html')
