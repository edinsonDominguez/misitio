from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_alcoba, name='Alcoba'),
    path('registro', views.get_producto, name='RegistroPro'),
    path('imagen', views.get_album, name='RegistroIma'),
    
]