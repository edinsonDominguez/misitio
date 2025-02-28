from django.urls import path
from home import views

urlpatterns =[
    path('', views.ver_inicio, name='Home'),
    path('productos', views.ver_productos, name='Productos'),
    path('informacion', views.ver_informacion, name='Informacion'),
    path('contacto', views.ver_contacto, name='Contacto'),
    path('mensaje', views.ver_mensaje_correo, name='mensaje_correo'),
    path('inf_producto/<int:producto_id>/', views.info_producto, name='inf_producto'),
    path('inf_categoria/<int:pk>/', views.info_categoria, name='categoria_producto'),
    path('producto_orden', views.info_precio, name='orden_precio'), 
    path('busqueda/', views.buscador, name='buscador'), 
]