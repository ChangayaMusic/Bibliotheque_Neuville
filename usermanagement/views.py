# views.py
from django.shortcuts import render, redirect

from usermanagement.models import CustomUser  # Import du modèle CustomUser
from usermanagement.forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from bibliotheque.models import Livre
import uuid
def add_reader_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Create the user instance but don't save it yet
            user = form.save(commit=False)
            # Set the username as a new UUID
            user.username = uuid.uuid4()  # Generate a unique UUID
            user.save()  # Save the user instance to the database
            return redirect('success_page')  # Redirect to the success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'add_reader.html', {'form': form})

def afficher_lecteurs(request):
    query = request.GET.get('q')  # Récupère le terme de recherche
    if query:
        lecteurs = CustomUser.objects.filter(
            nom__icontains=query
        ) | CustomUser.objects.filter(
            prenom__icontains=query
        ) | CustomUser.objects.filter(
            email__icontains=query
        )
    else:
        lecteurs = CustomUser.objects.all()

    # Ajoutez cette ligne pour déboguer
    print(f"Lecteurs: {lecteurs}")  # Vérifiez ce que contient la liste des lecteurs

    return render(request, 'lecteurs.html', {'lecteurs': lecteurs, 'query': query})

def afficher_livres(request, username):
    lecteur = get_object_or_404(CustomUser, username=username)
    livres = lecteur.livres.all()
    return render(request, 'livres.html', {'lecteur': lecteur, 'livres': livres})