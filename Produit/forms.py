# forms.py
from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = [ 'methode_livraison', 'adresse_livraison', 'quantite_commande']
