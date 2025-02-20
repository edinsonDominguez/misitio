from django.urls import path
from producto import views

urlpatterns = [
    path('registro', views.registrar_producto, name='RegistroPro'),
    path('vista_productos', views.ver_producto, name='ver_productos'),
    path('inicio', views.ver_inicio, name='inicio_usuario'),
    path('galeria', views.galeria_usuario, name='Galeria'),
    path('producto_usuario/<int:producto_id>', views.producto_usuario, name='producto_usuario'),
    path('eliminar_producto/<int:eliminar>', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:eliminar>', views.editar_producto, name='editar_producto')
    
]