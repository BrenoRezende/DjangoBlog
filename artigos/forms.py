from django import forms
from .models import Artigo

class NovoArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'slug', 'texto', 'banner']