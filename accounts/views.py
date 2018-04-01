from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def new_account_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:listar')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/create.html', {'form': form})
