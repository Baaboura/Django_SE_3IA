from django.contrib import admin
from .models import Produit, Commande
# Register your models here.

admin.site.register(Produit)

admin.site.register(Commande)