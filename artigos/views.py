from django.shortcuts import render
from .models import Artigo

def artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/index.html', {'artigos': artigos})

def artigo_detalhe_view(request, slug):
    artigo = Artigo.objects.get(slug = slug)
    return render(request, 'artigos/details.html', {'artigo': artigo})
