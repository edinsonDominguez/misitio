from django import forms

from .models import Categoria,Producto
from django.contrib.auth.models import User
class AlbumForm(forms.Form):
            
    nombre_album = forms.CharField(label='nombre', max_length=100, required=True)

    
    #producto = forms.ModelChoiceField(label='producto', queryset=Producto.objects.filter(usuario = User))

class ProductoForm(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=30)
    valor = forms.IntegerField(label='precio')
    inventario = forms.IntegerField(label='cantidad')
    categoria = forms.ModelChoiceField(label='categoria', queryset=Categoria.objects.all())
    descripcion = forms.CharField(label='descripcion', max_length=120, widget=forms.Textarea)
    medida = forms.CharField(label='medida (alto x ancho)', max_length=60)
    foto1 = forms.ImageField(label='foto1')
    foto2 = forms.ImageField(label='foto2', required=False)
    foto3 = forms.ImageField(label='foto3', required=False)
    foto4 = forms.ImageField(label='foto4', required=False)
    foto5 = forms.ImageField(label='foto5', required=False)
    foto6 = forms.ImageField(label='foto6', required=False)