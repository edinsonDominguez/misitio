from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
class Registro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro_user.html', {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario= form.save()
            login(request, usuario)
            return redirect('Login')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        
            return render(request, 'registro_user.html', {'form': form})

## ok
def cerrar_sesion(request):
    logout(request)
    return redirect('Ingreso')

##
def login_usuario(request):
    
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contra_usuario = form.cleaned_data.get('password')
            
            usuario = authenticate(username=nombre_usuario, password=contra_usuario)
            if usuario is not None:
                login(request, usuario)
                return redirect('Alcoba')
            else:
                messages.error(request, 'usuario no valido')
        else:
            messages.error(request, 'Ingresaste mal la informacion')
  
    form = AuthenticationForm()
    return render(request, 'login_user.html', {'form':form})


