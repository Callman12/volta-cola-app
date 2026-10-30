from django.db import models
from produits.models import Produit

class Commande(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente de validation'),
        ('validee', 'Validée'),
        ('en_cours_livraison', 'En cours de livraison'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    
    PAIEMENT_CHOICES = [
        ('orange_money', 'Orange Money'),
        ('mtn_momo', 'MTN MoMo'),
        ('wave', 'Wave'),
        ('carte', 'Carte Bancaire'),
        ('especes', 'Espèces à la livraison'),
    ]

    nom_client = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20)
    commune = models.CharField(max_length=100) # Ex: Cocody, Marcory, Plateau...
    quartier = models.CharField(max_length=100)
    point_repere = models.CharField(max_length=255, blank=True)
    creneau_livraison = models.CharField(max_length=100, default='Dès que possible')
    mode_paiement = models.CharField(max_length=50, choices=PAIEMENT_CHOICES)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='en_attente')
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    frais_livraison = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} - {self.nom_client} ({self.commune})"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantite}x {self.produit.nom} pour Commande #{self.commande.id}"
