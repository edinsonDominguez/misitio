from django.shortcuts import render

# Create your views here.

def ver_inicio(request):
    return render(request, 'home.html')