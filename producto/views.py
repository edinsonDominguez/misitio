from django.shortcuts import render, redirect
from .forms import Producto
# Create your views here.

def get_producto(request):
    if request.method == "POST":
        print ('si entro a get ')
        form = Producto(request.POST)
        if form.is_valid(): 
            print ('si valido')
            ## va la parte del registro de datos
            return redirect('Alcoba') # pagina que se a retornar 
    else:
        form = Producto()
    return render(request, 'registro_alcobas.html', {'form':form})    


def ver_alcoba(request):
    return render(request, 'alcobas.html')


#def registrar_alcobas(request):
 #   return render(request, 'registro_alcobas.html')
