# Generated by Django 4.2 on 2023-09-15 14:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('activite_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='activite/')),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age_minimum', models.IntegerField()),
                ('capacite_max', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('employe_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('statut', models.CharField(choices=[('disponible', 'Disponible'), ('non_disponible', 'Non Disponible')], default='disponible', max_length=20)),
                ('email_employee', models.EmailField(default='example@example.com', max_length=254)),
                ('telephone', models.CharField(default='+212060000000', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('equipement_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_achat', models.DateField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('etat', models.CharField(choices=[('en_service', 'En service'), ('hors_service', 'Hors service'), ('en_reparation', 'En réparation')], default='en_service', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Statistique',
            fields=[
                ('statistique_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('participants', models.PositiveIntegerField()),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.activite')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_reservation', models.DateTimeField(auto_now_add=True)),
                ('date_activite', models.DateTimeField()),
                ('nom_client', models.CharField(max_length=100)),
                ('email_client', models.EmailField(max_length=254)),
                ('telephone_client', models.CharField(max_length=20)),
                ('nombre_participants', models.PositiveIntegerField()),
                ('statut', models.CharField(choices=[('en_attente', 'En Attente'), ('validee', 'Validée'), ('annulee', 'Annulée')], default='en_attente', max_length=20)),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.activite')),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('statistique_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('contenu', models.TextField()),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.activite')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_paiement', models.CharField(choices=[('carte', 'Carte'), ('especes', 'Espèces'), ('autres', 'Autres')], max_length=10)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.reservation')),
            ],
        ),
    ]
