from django.db import models
from datetime import date
from datetime import timedelta

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom du médecin")
    mobile = models.CharField(max_length=15, unique=True, verbose_name="Numéro de téléphone")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="Email")
    specialite = models.CharField(max_length=100, verbose_name="Spécialité")
    adresse = models.TextField(null=True, blank=True, verbose_name="Adresse")

    def __str__(self):
        return f"{self.name} - {self.specialite}"
   
    
    
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('Autre', 'Autre'),
    ]

    name = models.CharField(max_length=100)  # Nom du patient
    date_naissance = models.DateField(null=True, blank=True)  # Date de naissance
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # Genre
    mobile = models.CharField(max_length=15, unique=True)  # Téléphone
    adresse = models.TextField(null=True, blank=True)  # Adresse
   
    def __str__(self):
        return f"{self.name} - {self.gender}"

      
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()  # Stocke seulement la date
    time = models.TimeField()  # Stocke seulement l'heure

    def __str__(self):
        return f"Rendez-vous : {self.doctor.name} avec {self.patient.name} le {self.date} à {self.time}"

     
class Mother(models.Model):
    """ Modèle pour la mère du nouveau-né """
    name = models.CharField(max_length=100)  # Nom de la mère
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)


class Father(models.Model):
    """ Modèle pour le père du nouveau-né """
    name = models.CharField(max_length=100)  # Nom du père
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    
class Newborn(models.Model):
    """ Modèle pour le nouveau-né avec plus d'infos sur l'accouchement et la santé du bébé """
    name = models.CharField(max_length=100)
    date_naissance = models.DateField()
    heure_naissance = models.TimeField(null=True, blank=True, help_text="Heure de naissance")
    gender = models.CharField(max_length=10, choices=[('M', 'Garçon'), ('F', 'Fille')])
    poids = models.DecimalField(max_digits=5, decimal_places=2, help_text="Poids en kg")
    taille = models.DecimalField(max_digits=5, decimal_places=2, help_text="Taille en cm")

    # Parents
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
    father = models.ForeignKey(Father, on_delete=models.CASCADE, null=True, blank=True)

    # Accouchement
    LIEU_NAISSANCE_CHOICES = [('hopital', 'Hôpital'), ('clinique', 'Clinique'), ('domicile', 'Domicile')]
    lieu_naissance = models.CharField(max_length=20, choices=LIEU_NAISSANCE_CHOICES, default='hopital')

    TYPE_ACCOUCHEMENT_CHOICES = [('voie_basse', 'Accouchement par voie basse'), ('cesarienne', 'Césarienne'), ('forceps', 'Forceps ou ventouse')]
    type_accouchement = models.CharField(max_length=20, choices=TYPE_ACCOUCHEMENT_CHOICES)

    duree_travail = models.DurationField(null=True, blank=True, help_text="Durée du travail avant l'accouchement")
    complications = models.TextField(null=True, blank=True, help_text="Complications éventuelles")

    # Santé du bébé
    score_apgar_1min = models.IntegerField(null=True, blank=True, help_text="Score APGAR à 1 min (0-10)")
    score_apgar_5min = models.IntegerField(null=True, blank=True, help_text="Score APGAR à 5 min (0-10)")
    score_apgar_10min = models.IntegerField(null=True, blank=True, help_text="Score APGAR à 10 min (0-10)")
    
    reanimation = models.BooleanField(default=False, help_text="Réanimation nécessaire après la naissance ?")
    groupe_sanguin = models.CharField(max_length=5, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], null=True, blank=True)

    frequence_cardiaque = models.IntegerField(null=True, blank=True, help_text="Fréquence cardiaque du bébé (battements par minute)")
    frequence_respiratoire = models.IntegerField(null=True, blank=True, help_text="Fréquence respiratoire (respirations par minute)")
    
    vaccins = models.TextField(null=True, blank=True, help_text="Vaccins administrés à la naissance")
    antecedents_familiaux = models.TextField(null=True, blank=True, help_text="Antécédents médicaux familiaux importants")

    # Suivi post-natal
    allaitement = models.CharField(max_length=20, choices=[('maternel', 'Allaitement maternel'), ('artificiel', 'Allaitement artificiel'), ('mixte', 'Mixte')], null=True, blank=True)
    date_sortie = models.DateField(null=True, blank=True, help_text="Date de sortie de l'hôpital")

    # Médecin responsable
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Né le {self.date_naissance})"
class Medicament(models.Model):
    nom = models.CharField(max_length=100)  
    description = models.TextField(null=True, blank=True)  
    categorie = models.CharField(max_length=100, choices=[
        ('antibiotique', 'Antibiotique'),
        ('antalgique', 'Antalgique'),
        ('anti-inflammatoire', 'Anti-inflammatoire'),
        ('vitamines', 'Vitamines'),
        ('autres', 'Autres')
    ])  
    quantite_stock = models.PositiveIntegerField()  
    prix = models.DecimalField(max_digits=10, decimal_places=2)  
    date_expiration = models.DateField()  

    def montant_total_stock(self):
        """ Calcule le montant total du stock """
        return self.quantite_stock * self.prix

    def etat_stock(self):
        """ Évalue l'état du stock """
        if self.quantite_stock == 0:
            return "⚠️ Rupture de stock"
        elif self.quantite_stock < 10:
            return "🔴 Faible"
        elif self.quantite_stock < 50:
            return "🟠 Moyen"
        else:
            return "🟢 Plein"

    def est_presque_expire(self):
        """ Vérifie si le médicament expire dans 30 jours """
        return self.date_expiration <= date.today() + timedelta(days=30)

    def est_expire(self):
        """ Vérifie si le médicament est expiré """
        return self.date_expiration < date.today()

    def __str__(self):
        return f"{self.nom} (Expire le {self.date_expiration})"
    
    
    
from django.db import models

class Facture(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)  # Relier au patient
    date = models.DateField(auto_now_add=True)  # Date automatique
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de la facture
    description = models.TextField(blank=True, null=True)  # Description facultative

    def __str__(self):
        return f"Facture #{self.id} - {self.patient.name} ({self.date})"
    