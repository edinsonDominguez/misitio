from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    inventario = models.IntegerField()
    estado = models.BooleanField(auto_created=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.inventario)