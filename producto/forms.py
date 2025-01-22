from django import forms

class Album(forms.Form):
    nombre_album = forms.CharField(label='nombre', max_length=100)
    foto1 = forms.ImageField(label='foto1')
    foto2 = forms.ImageField(label='foto2')
    foto3 = forms.ImageField(label='foto3')
    foto4 = forms.ImageField(label='foto4')
    foto5 = forms.ImageField(label='foto5')
    foto6 = forms.ImageField(label='foto6')

class Producto(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    valor = forms.IntegerField(label='precio')
    inventario = forms.IntegerField(label='cantidad')
    