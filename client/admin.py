from django.contrib import admin
from .models import *

# Register your models here.

class AdminPatient(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email','sexe', 'age', 'service')
 
class AdminHabitude(admin.ModelAdmin):
    list_display = ('user','jour', 'heure', 'repas', 'boisson', 'lieux')
    
class AdminRoom(admin.ModelAdmin):
    list_display = ('name','date','save_by')
    
class AdminMessage(admin.ModelAdmin):
    list_display = ('value','date', 'user', 'room')
    
    
admin.site.register(Patient, AdminPatient)
admin.site.register(HabitudeAlimentaire, AdminHabitude)
admin.site.register(Room,AdminRoom)
admin.site.register(Message,AdminMessage)
    
