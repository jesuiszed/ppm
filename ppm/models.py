from django.db import models
from datetime import date

class Activite(models.Model):

    activite_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='activite/', blank=True, null=True)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    age_minimum = models.IntegerField()
    capacite_max = models.IntegerField()

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En Attente'),
        ('validee', 'Validée'),
        ('annulee', 'Annulée'),
    ]

    reservation_id = models.AutoField(primary_key=True)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    date_activite = models.DateTimeField()
    nom_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    telephone_client = models.CharField(max_length=20)
    nombre_participants = models.PositiveIntegerField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')

    def __str__(self):
        return f"Réservation pour {self.nom_client} - {self.activite.nom}"

class Employe(models.Model):
    STATUT_CHOICES = [
        ('disponible', 'Disponible'),
        ('non_disponible', 'Non Disponible'),
    ]

    employe_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo/', blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='disponible')
    email_employee = models.EmailField(default='example@example.com')  # Define a default value
    telephone = models.CharField(max_length=20 , default='+212060000000')

    def __str__(self):
        return self.nom

class Paiement(models.Model):
    activite = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    TYPE_PAIEMENT_CHOICES = (
        ('carte', 'Carte'),
        ('especes', 'Espèces'),
        ('autres', 'Autres'),
    )
    type_paiement = models.CharField(max_length=10, choices=TYPE_PAIEMENT_CHOICES)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Paiement pour {self.activite.nom} - {self.get_type_paiement_display()}"

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=200)

    def __str__(self):
        return f"Contact de {self.nom} - {self.role}"

class Statistique(models.Model):
    statistique_id = models.AutoField(primary_key=True)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    participants = models.PositiveIntegerField()

    def __str__(self):
        return f"Statistique pour {self.activite.nom} le {self.date}"

class Rapport(models.Model):
    rapport_id = models.AutoField(primary_key=True)
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    contenu = models.TextField()

    def __str__(self):
        return f"Rapport pour {self.activite.nom} le {self.date}"


class Equipement(models.Model):
    ETAT_CHOICES = (
        ('en_service', 'En service'),
        ('hors_service', 'Hors service'),
        ('en_reparation', 'En réparation'),
    )

    equipement_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_achat = models.DateField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='en_service')

    def __str__(self):
        return self.nom