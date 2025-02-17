from django.urls import path
from producto import views

urlpatterns = [
    path('', views.ver_alcoba, name='Alcoba'),
    path('registro', views.registrar_producto, name='RegistroPro'),
    path('vista_productos', views.ver_producto, name='ver_productos'),
    path('inicio', views.ver_inicio, name='inicio_usuario'),
    path('galeria', views.galeria_usuario, name='Galeria'),
    
]