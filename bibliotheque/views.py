from django.shortcuts import render, redirect, get_object_or_404
from .forms import LivreForm, PretForm 
from .models import Livre
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .models import Livre

def test_view(request):
    return HttpResponse("Test view works!")

def home_view(request):
    return render(request, 'home.html')


def add_book_view(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)  # Instanciation du formulaire
        if form.is_valid():
            form.save()
            messages.success(request, "Le livre a été ajouté avec succès.")
            return redirect('success_page')
        else:
            print(form.errors)
            messages.error(request, "Il y a des erreurs dans le formulaire.")
            return render(request, 'add_book.html', {'form': form})
    else:
        form = LivreForm()  # Instanciation du formulaire
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



def liste_livres(request):
    query = request.GET.get('q')  # Récupérer le terme de recherche depuis l'URL
    livres = Livre.objects.all()

    # Si une requête de recherche est présente, filtrer les livres
    if query:
        livres = livres.filter(
            Q(titre__icontains=query) |  # Chercher par titre
            Q(auteur__icontains=query)   # Chercher par auteur
        )

    return render(request, 'liste_livres.html', {'livres': livres, 'query': query})

def pret(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    if request.method == 'POST':
        form = PretForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            messages.success(request, "Les informations du livre ont été mises à jour avec succès.")
            return redirect('liste_livres')  # Remplacez par le nom de votre vue de liste de livres
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = PretForm(instance=livre)
    
    return render(request, 'pret.html', {'form': form})

