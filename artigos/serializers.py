from rest_framework import serializers
from .models import Artigo

class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        depth = 1
        fields = ['id', 'titulo', 'texto', 'data', 'autor']