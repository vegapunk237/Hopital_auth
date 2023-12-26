from django.contrib import admin
from .models import *

# Register your models here.

class AdminPatient(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'Adresse', 'phone', 'sex', 'age', 'city', 'created_date', 'save_by')
 
class AdminHabitude(admin.ModelAdmin):
    list_display = ('user','jour', 'heure', 'repas', 'boisson', 'lieux')
    
admin.site.register(Patient, AdminPatient)
admin.site.register(HabitudeAlimentaire, AdminHabitude)
    
