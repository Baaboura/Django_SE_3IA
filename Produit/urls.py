from django.urls import path
from . import views

urlpatterns = [
    path("", views.produit_list, name='produit_list'),
    path('add-to-commande/', views.click_button_add_to_commande, name='click_button_add_to_commande'),
path('delete_commande/<int:id>/', views.delete_commande, name='delete_commande'),
    path('edit_commande/<int:commande_id>/', views.edit_commande, name='edit_commande'),
]
