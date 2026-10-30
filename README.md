# 🥤 VOLTA Cola App

Application web et backend Django pour la gestion et la vente de **VOLTA Cola**, la marque de cola qui réveille Abidjan ! Conçue pour le projet de Licence 3 en Génie Logiciel (IIT).

## 🚀 Fonctionnalités principales
- **Catalogue produits :** Canettes 33 cl, Bouteilles 50 cl & 1,5 L, Packs (6 ou 24), Gamme Zéro Sucre et Édition Cerise.
- **Gestion des commandes :** Commandes en ligne, suivi en temps réel, choix des créneaux de livraison à Abidjan et paiement (Mobile Money / Espèces).
- **Espace Revendeurs :** Inscription des professionnels (maquis, boutiques, événements), tarifs dégressifs et commandes en gros.
- **Gestion des stocks :** Suivi des stocks par entrepôt/site, alertes de réapprovisionnement et mouvements de stock.

## 🛠️ Stack Technique
- **Backend :** Python 3.10+ / Django 4.2 / Django REST Framework
- **Base de données :** PostgreSQL
- **Gestion de configuration :** python-decouple
- **Serveur statique :** WhiteNoise

## 📦 Installation et exécution locale

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Callman12/volta-cola-app.git
   cd volta-cola-app
   ```

2. **Créer et activer l'environnement virtuel :**
   ```bash
   python -m venv .venv
   # Sur Windows :
   .venv\Scripts\activate
   # Sur Linux/Mac :
   source .venv/bin/activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement :**
   Copier `.env.example` en `.env` et renseigner vos accès PostgreSQL.
   ```bash
   cp .env.example .env
   ```

5. **Appliquer les migrations :**
   ```bash
   python manage.py migrate
   ```

6. **Lancer le serveur de développement :**
   ```bash
   python manage.py runserver
   ```

---
*Développé par Calman pour Elie Pethuel (IIT - L3 Génie Logiciel).*
