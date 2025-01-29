from django.urls import path
from .views import ver_inicio

urlpatterns =[
    path('', ver_inicio, name='Home'),
]