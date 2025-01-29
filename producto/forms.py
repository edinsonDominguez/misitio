from django import forms

from .models import Categoria, User, Producto

class AlbumForm(forms.Form):
    nombre_album = forms.CharField(label='nombre', max_length=100, required=True)
    foto1 = forms.ImageField(label='foto1', required=False)
    foto2 = forms.ImageField(label='foto2', required=False)
    foto3 = forms.ImageField(label='foto3', required=False)
    foto4 = forms.ImageField(label='foto4', required=False)
    foto5 = forms.ImageField(label='foto5', required=False)
    foto6 = forms.ImageField(label='foto6', required=False)
    producto = forms.ModelChoiceField(label='producto', queryset=Producto.objects.all())

class Producto(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    valor = forms.IntegerField(label='precio')
    inventario = forms.IntegerField(label='cantidad')
    categoria = forms.ModelChoiceField(label='categoria', queryset=Categoria.objects.all())
    usuario = forms.ModelChoiceField(label='usuario', queryset=User.objects.all())