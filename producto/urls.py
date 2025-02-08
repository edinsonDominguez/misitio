from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_alcoba, name='Alcoba'),
    path('registro', views.registrar_producto, name='RegistroPro'),
    path('imagen', views.get_album, name='RegistroIma'),
    path('registro_producto', views.ver_producto, name='ver_productos'),
    path('registro_album', views.ver_album, name='ver_albumnes'),
    path('inicio', views.ver_inicio, name='Inicio'),
    
]