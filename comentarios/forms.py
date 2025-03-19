from django import forms

class ComentarioForm(forms.Form):
    comentario = forms.CharField(label='comentario', max_length=150, widget=forms.Textarea)