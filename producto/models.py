from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s' % (self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    inventario = models.IntegerField()
    estado = models.BooleanField(default=True)
    categoria_producto = models.ForeignKey(Categoria, on_delete = models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.nombre)

class Imagen(models.Model):
    nombre_album = models.CharField(max_length=30, null=True, blank=True)
    foto1 = models.ImageField(upload_to='producto', null=True, blank=True)
    foto2 = models.ImageField(upload_to='producto', null=True, blank=True)
    foto3 = models.ImageField(upload_to='producto', null=True, blank=True)
    foto4 = models.ImageField(upload_to='producto', null=True, blank=True)
    foto5 = models.ImageField(upload_to='producto', null=True, blank=True)
    foto6 = models.ImageField(upload_to='producto', null=True, blank=True)
    producto_imagen = models.ForeignKey(Producto, on_delete = models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return '%s' % (self.foto1)

    
    