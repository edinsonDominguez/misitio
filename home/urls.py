from django.urls import path
from home import views

urlpatterns =[
    path('', views.ver_inicio, name='Home'),
    path('productos', views.ver_productos, name='Productos'),
    path('informacion', views.ver_informacion, name='Informacion'),
    path('contacto', views.ver_contacto, name='Contacto'),
    path('mensaje', views.ver_mensaje_correo, name='mensaje_correo'),
    path('inf_producto/<int:producto_id>/', views.info_producto, name='inf_producto')
    
]