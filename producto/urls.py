from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_alcoba, name='Alcoba'),
    path('registro', views.registrar_producto, name='RegistroPro'),
    path('imagen', views.get_album, name='RegistroIma'),
    path('registro_producto', views.ver_registro, name='ver_lista'),
    path('inicio', views.ver_inicio, name='Inicio'),
    
]