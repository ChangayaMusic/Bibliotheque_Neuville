# forms.py

from django import forms
from .models import Livre
from django.utils import timezone
from usermanagement.models import CustomUser

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'date_publication', 'genre', 'format']

class PretForm(forms.ModelForm):
    lecteur = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        label='Lecteur'
    )
    # Le champ 'date_pret' est retiré du formulaire car il sera défini sur la date/heure actuelle automatiquement

    class Meta:
        model = Livre
        fields = ['lecteur']

    def save(self, commit=True):
        livre = super().save(commit=False)
        if self.cleaned_data['lecteur'] is None:
            livre.pret = False
        else:
            livre.pret = True
        livre.date_pret = timezone.now()  # Définir automatiquement 'date_pret' sur la date/heure actuelle
        if commit:
            livre.save()
        return livre
