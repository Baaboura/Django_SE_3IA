# Generated by Django 5.1.3 on 2024-11-07 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
        ('Produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produit.produit')),
            ],
        ),
    ]