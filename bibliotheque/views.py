from django.shortcuts import render, redirect, get_object_or_404
from .forms import LivreForm  # Importez le formulaire LivreForm depuis le même répertoire
from .models import Livre
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test view works!")

def home_view(request):
    return render(request, 'home.html')

def add_book_view(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirection vers la page de succès
            return redirect('success_page')
        else:
            # Redirection vers la page d'erreur si le formulaire est invalide
            return redirect('error_page')
    else:
        form = LivreForm()
    return render(request, 'add_book.html', {'form': form})

def modify_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            # Redirection vers la page de succès
            return redirect('success_page')
        else:
            # Redirection vers la page d'erreur si le formulaire est invalide
            return redirect('error_page')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'modify_book.html', {'form': form})

def error_page(request):
    return render(request, 'error.html')

def success_page(request):
    return render(request, 'success.html')
