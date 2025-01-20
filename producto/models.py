from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s' % (self.nombre)

class Imagen(models.Model):
    foto1 = models.ImageField(upload_to='producto')
    foto2 = models.ImageField(upload_to='producto')
    foto3 = models.ImageField(upload_to='producto')
    foto4 = models.ImageField(upload_to='producto')
    foto5 = models.ImageField(upload_to='producto')
    foto6 = models.ImageField(upload_to='producto')
    
    def __str__(self):
        return '%s' % (self.foto1)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    inventario = models.IntegerField()
    estado = models.BooleanField(default=True)
    categoria_producto = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    imagen_producto = models.ForeignKey(Imagen, on_delete = models.CASCADE)
    

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.valor, self.fecha_registro)
    
    