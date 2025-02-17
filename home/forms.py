from django import forms


class FormContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=40, required=True)
    correo = forms.EmailField(label='Correo', required=True)
    comentario = forms.CharField(label='Escribenos aqui', required=True, widget=forms.Textarea)
