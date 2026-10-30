from django.db import models
from produits.models import Produit

class Entrepots(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    localisation = models.CharField(max_length=255)
    responsable = models.CharField(max_length=150)

    def __str__(self):
        return f"Entrepôt {self.nom} ({self.localisation})"

class Stock(models.Model):
    entrepot = models.ForeignKey(Entrepots, on_delete=models.CASCADE, related_name='stocks')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='stocks')
    quantite = models.PositiveIntegerField(default=0)
    seuil_alerte = models.PositiveIntegerField(default=50)
    derniere_maj = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('entrepot', 'produit')

    def __str__(self):
        return f"{self.produit.nom} @ {self.entrepot.nom} : {self.quantite} unités"

class MouvementStock(models.Model):
    TYPE_MOUVEMENT = [
        ('entree', 'Entrée (Production / Approvisionnement)'),
        ('sortie', 'Sortie (Vente / Livraison)'),
        ('ajustement', 'Ajustement inventaire'),
    ]

    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    entrepot = models.ForeignKey(Entrepots, on_delete=models.CASCADE)
    type_mouvement = models.CharField(max_length=20, choices=TYPE_MOUVEMENT)
    quantite = models.PositiveIntegerField()
    motif = models.CharField(max_length=255)
    date_mouvement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_mouvement_display()} : {self.quantite}x {self.produit.nom}"
