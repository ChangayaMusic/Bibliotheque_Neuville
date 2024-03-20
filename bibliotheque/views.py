# views.py

from django.shortcuts import render, redirect, get_object_or_404
from bibliotheque.forms import LivreForm
from .models import Livre

def home_view(request):
    return render(request, 'home.html')


def add_book_view(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the home page
            return redirect('home')
    else:
        form = LivreForm()
    return render(request, 'add_book.html', {'form': form})

def modify_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('view_livre', livre_id=livre_id)  # Redirect to the view page for the modified livre
    else:
        form = LivreForm(instance=livre)
    return render(request, 'modify_book.html', {'form': form})
