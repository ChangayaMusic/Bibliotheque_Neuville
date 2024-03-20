from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_inscription = models.DateField(auto_now_add=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"