from django.shortcuts import render, redirect
from .models import Artigo
from django.contrib.auth.decorators import login_required
from .forms import NovoArtigoForm

def artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/index.html', {'artigos': artigos})

def artigo_detalhe_view(request, slug):
    artigo = Artigo.objects.get(slug = slug)
    return render(request, 'artigos/details.html', {'artigo': artigo})

@login_required(login_url='accounts:login')
def artigos_novo_view(request):
    if request.method == 'POST':
        form = NovoArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigos:listar')
    else:
        form = NovoArtigoForm()
    
    return render(request, 'artigos/create.html', {'form': form})
