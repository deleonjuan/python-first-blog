from django import forms

from .models import Publicacion

class Publicacion_formulario(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'texto',)