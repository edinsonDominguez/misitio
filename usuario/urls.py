from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_usuario, name='Registro'),
    path('login_user', views.login_usuario, name='Login')

]