from django.db import models
from Client.models import Client
# Create your models here.

class Produit(models.Model):

    nom_produit= models.CharField(max_length=50)
    quantite_produit= models.IntegerField()
    description_produit= models.TextField()
    prix_produit= models.FloatField()
    date_publication_produit= models.DateField(auto_now=True)
    date_expiration_produit= models.DateField(auto_now=True)

class Commande(models.Model):

    produit_commande= models.ForeignKey(Produit, on_delete=models.CASCADE)
    client_commande= models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande= models.DateField(auto_now=True)
    date_livraison= models.DateField(auto_now=True)
    methode_livraison= models.CharField(max_length=50,default='Express')
    adresse_livraison= models.CharField(max_length=50,default='Tunis')
    quantite_commande= models.IntegerField()


    pass