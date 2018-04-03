from django.shortcuts import render
from .models import Artigo
from django.contrib.auth.decorators import login_required

def artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/index.html', {'artigos': artigos})

def artigo_detalhe_view(request, slug):
    artigo = Artigo.objects.get(slug = slug)
    return render(request, 'artigos/details.html', {'artigo': artigo})

@login_required(login_url='accounts:login')
def artigos_novo_view(request):
    return render(request, 'artigos/create.html')
