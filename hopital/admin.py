from django.contrib import admin
from .models import Patient, Doctor, Appointment, Mother, Father, Newborn, Medicament
from django.utils.html import format_html

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialite', 'mobile', 'email', 'adresse')
    search_fields = ('name', 'specialite', 'mobile', 'email')
    list_filter = ('specialite',)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_naissance', 'gender', 'mobile',  'adresse')
    search_fields = ('name', 'mobile',)
    list_filter = ('gender',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'date', 'time')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('date',)


@admin.register(Mother)
class MotherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email', 'adresse')
    search_fields = ('name', 'mobile', 'email')


@admin.register(Father)
class FatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email', 'adresse')
    search_fields = ('name', 'mobile', 'email')


@admin.register(Newborn)
class NewbornAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_naissance', 'gender', 'poids', 'taille', 'lieu_naissance', 'type_accouchement', 'mother', 'doctor')
    search_fields = ('name', 'mother__name', 'father__name')
    list_filter = ('gender', 'lieu_naissance', 'type_accouchement', 'date_naissance')





@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'quantite_stock', 'prix', 'montant_total_stock', 'date_expiration', 'alerte_expiration', 'etat_stock')
    search_fields = ('nom', 'categorie')
    list_filter = ('categorie', 'date_expiration')

    def montant_total_stock(self, obj):
        return f"{obj.montant_total_stock()} FCFA"

    def etat_stock(self, obj):
        return obj.etat_stock()

    def alerte_expiration(self, obj):
        """ Affiche une alerte si le médicament est expiré ou proche de l'expiration """
        if obj.est_expire():
            return format_html('<span style="color: red; font-weight: bold;">❌ Expiré</span>')
        elif obj.est_presque_expire():
            return format_html('<span style="color: orange; font-weight: bold;">⚠️ Expire bientôt</span>')
        else:
            return format_html('<span style="color: green;">✅ OK</span>')

    montant_total_stock.short_description = "Montant total"
    etat_stock.short_description = "État du stock"
    alerte_expiration.short_description = "Expiration"
