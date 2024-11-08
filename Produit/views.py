from django.http import HttpResponse
from django.template import loader
from .models import Produit,Commande
from django.shortcuts import render
from django.utils import timezone
from Client.models import Client
from django.urls import reverse



def produit_list(request):
    template = loader.get_template('DisplayProduit.html')
    produits = Produit.objects.all().values()  # Query all Produit objects
    commandes = Commande.objects.all().values()
    context = {
        'produits': produits,
        'commandes': commandes
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import redirect, get_object_or_404


def click_button_add_to_commande(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')

        # Retrieve the product by its ID
        produit = get_object_or_404(Produit, id=produit_id)

        # Retrieve the client where the name is "abc"
        client = get_object_or_404(Client, nom="abc")  # Assuming 'nom' is the field for the client's name

        # Create the order (commande)
        commande = Commande.objects.create(
            produit=produit,
            client=client,
            quantite_commande=request.POST.get('quantite_commande', 1),  # Assuming the quantity is passed in the form
            date_livraison=request.POST.get('date_livraison')  # Ensure you handle date of delivery correctly
        )

        return redirect('produit_list')  # Redirect to the product list after adding the order

    return render(request, 'produit_list.html')  # Or your appropriate template

def delete_commande(request, id):
    # Check if the request is a POST request
    if request.method == "POST":
        # Retrieve the specific command by ID
        commande = get_object_or_404(Commande, id=id)
        # Delete the command
        commande.delete()
        # Redirect back to the page with the command list
        return redirect(reverse('produit_list'))  # Use the appropriate name for your command list view

    # If the request is not POST, redirect to the list page or show an error
    return redirect(reverse('produit_list'))


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Commande
from .forms import CommandeForm  # Import the form you'll create for editing

from django.shortcuts import redirect


def edit_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            # Redirection vers la page 'produit_list' après la soumission
            return redirect('produit_list')
    else:
        form = CommandeForm(instance=commande)

    return render(request, 'edit_commande.html', {'form': form})