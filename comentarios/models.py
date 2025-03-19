from django.db import models
from producto.models import Producto
from django.contrib.auth.models import User

# Create your models here.
class Comentarios(models.Model):
    comentario = models.CharField(max_length=150)
    fecha_ingreso = models.DateField(auto_now=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True) # el producto del comentario
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # el cliente que dejara el comentario
