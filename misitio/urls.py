"""
URL configuration for misitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import primera_pagina, hora_actual, suma_hora, nombre_usuario, persona, persona_sistema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primera_pagina, name = 'Home'),
    path('hora', hora_actual, name = 'Hora'),
    path('suma_hora/<numero>', suma_hora, name = 'Suma'),
    path('nombre/<nombre>', nombre_usuario, name = 'Nombre'),
    path('persona', persona, name = 'Persona'),
    path('persona_sistema', persona_sistema, name = 'Persona2'),
    

]
