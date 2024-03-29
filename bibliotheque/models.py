from django.db import models

# Create your models here.
from django.db import models
from usermanagement.models import CustomUser




class Livre(models.Model):
    TITRE_CHOICES = [
        ('Roman', 'Roman'),
        ('Nouvelle', 'Nouvelle'),
        ('Conte', 'Conte'),
        ('Science-fiction', 'Science-fiction'),
        ('Fantaisie', 'Fantaisie'),
        ('Mystère', 'Mystère'),
        ('Policier', 'Policier'),
        ('Horreur', 'Horreur'),
        ('Biographie', 'Biographie'),
        ('Autobiographie', 'Autobiographie'),
        ('Essai', 'Essai'),
        ('Livre de référence', 'Livre de référence'),
        ('Livre de voyage', 'Livre de voyage'),
        ('Livre d\'histoire', 'Livre d\'histoire'),
        ('Livre de sciences', 'Livre de sciences'),
        ('Poésie', 'Poésie'),
        ('Science', 'Science'),
        ('Religion et spiritualité', 'Religion et spiritualité'),
        ('Arts et divertissement', 'Arts et divertissement'),
        ('Santé et bien-être', 'Santé et bien-être'),
        ('Éducation et apprentissage', 'Éducation et apprentissage'),
        ('Economie', 'Economie'),
        ('Politique et société', 'Politique et société'),
        # Add more genres if needed
    ]

    FORMAT_CHOICES = [
        ('Poche', 'Poche'),
        ('Normal', 'Normal'),
        # Add more format choices if needed
    ]

    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    date_publication = models.IntegerField()
    genre = models.CharField(max_length=50, choices=TITRE_CHOICES)
    date_ajout = models.DateField(auto_now_add=True)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    pret = models.BooleanField(default=False)
    date_pret = models.DateField(null=True, blank=True)
    lecteur = models.ForeignKey('usermanagement.CustomUser', on_delete=models.CASCADE, related_name='livres', null=True,
                                blank=True)

    def __str__(self):
        return self.titre