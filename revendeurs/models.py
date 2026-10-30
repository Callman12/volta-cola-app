from django.db import models

class Revendeur(models.Model):
    TYPE_CHOICES = [
        ('maquis', 'Maquis / Restaurant'),
        ('boutique', 'Boutique / Épicerie'),
        ('superette', 'Superette / Supermarché'),
        ('evenement', 'Organisateur d’événements'),
    ]

    nom_etablissement = models.CharField(max_length=150)
    nom_responsable = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    type_etablissement = models.CharField(max_length=50, choices=TYPE_CHOICES)
    commune = models.CharField(max_length=100)
    adresse = models.TextField()
    valide = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_etablissement} ({self.get_type_etablissement_display()}) - {self.commune}"
