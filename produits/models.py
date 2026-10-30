from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True) # Ex: Original, Zéro Sucre, Cerise, Packs
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    FORMAT_CHOICES = [
        ('canette_33', 'Canette 33 cl'),
        ('bouteille_50', 'Bouteille 50 cl'),
        ('bouteille_150', 'Bouteille 1,5 L'),
        ('pack_6', 'Pack 6 canettes'),
        ('pack_24', 'Pack fête 24'),
    ]

    nom = models.CharField(max_length=150)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    format_bouteille = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2) # En FCFA
    description = models.TextField(blank=True)
    disponible = models.BooleanField(default=True)
    image_url = models.URLField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.get_format_bouteille_display()}) - {self.prix_unitaire} FCFA"
