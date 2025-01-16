from django import forms


class Producto(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    valor = forms.IntegerField(label='precio')
    inventario = forms.IntegerField(label='cantidad')
    foto = forms.ImageField(label='imagen')