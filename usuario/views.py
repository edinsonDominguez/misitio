from django.shortcuts import render

# Create your views here.

def registrar_usuario(request):
    return render(request, 'registro_user.html')

def login_usuario(request):
    return render(request, 'login_user.html')


