from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length='30')
    valor = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    inventario = models.IntegerField()
    estado = models.BooleanField(auto_created=True)