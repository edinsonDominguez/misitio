from django.db import models

# Create your models here.

<<<<<<< HEAD
=======
<<<<<<< HEAD
class Usuario(models.Model):

    id_usuario = models.CharField(max_length=11)
    nombre_usuario = models.CharField(max_length=30)
    apellido_usuario = models.CharField(max_length=30)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=12)
    password = models.CharField(max_length=15)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)
    headshot = models.ImageField(upload_to='usuario')
    admin = models.BooleanField(auto_created=False)

    def __str__(self):
        return '%s %s' % (self.nombre_usuario, self.apellido_usuario)

=======
>>>>>>> usuario
class Producto(models.Model):
    nombre = models.CharField(max_length='30')
    valor = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    inventario = models.IntegerField()
<<<<<<< HEAD
    estado = models.BooleanField(auto_created=True)
=======
    estado = models.BooleanField(auto_created=True)
>>>>>>> alcoba
>>>>>>> usuario
