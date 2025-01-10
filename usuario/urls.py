from django.urls import path
<<<<<<< HEAD
from .views import Registro, login_usuario, cerrar_sesion

urlpatterns = [
    path('', Registro.as_view(), name='Ingreso'),
    path('cerrar_sesion', cerrar_sesion, name = 'cerrar_sesion'),
    path('login_user', login_usuario, name='Login'),
=======
from . import views

urlpatterns = [
    path('', views.ver_alcoba, name='Alcoba'),
    path('registro', views.registrar_alcobas, name='Alcoba')
>>>>>>> alcoba

]