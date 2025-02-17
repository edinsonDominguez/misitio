from django.urls import path
from home import views

urlpatterns =[
    path('', views.ver_inicio, name='Home'),
    path('productos', views.ver_productos, name='Productos'),
    path('informacion', views.ver_informacion, name='Informacion'),
    path('contacto', views.ver_contacto, name='Contacto'),
]