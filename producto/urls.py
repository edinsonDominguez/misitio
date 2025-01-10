
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_alcoba, name='Alcoba'),
    path('registro', views.registrar_alcobas, name='Alcoba')

]