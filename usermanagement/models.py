from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



class CustomUser(AbstractUser):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_inscription = models.DateField(auto_now_add=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    username = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   



    def __str__(self):
        return f"{self.prenom} {self.nom}"
