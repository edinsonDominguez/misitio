from django.urls import path
from .views import Registro, login_usuario, cerrar_sesion

urlpatterns = [
    path('', Registro.as_view(), name='Ingreso'),
    
    path('login_user', login_usuario, name='Login'),
    
    path('cerrar_sesion', cerrar_sesion, name = 'cerrar_sesion'),
]

