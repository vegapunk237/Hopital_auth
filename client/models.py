from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    
    nom = models.CharField(max_length=132)
    
    prenom = models.CharField(max_length=100)
    
    email = models.EmailField()
    
    Adresse = models.CharField(max_length=100)
    
    phone = models.CharField(max_length=100)
    
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    
    age = models.CharField(max_length = 12)
    
    city = models.CharField(max_length=32)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
    def __str__(self):
        return self.nom
    
class HabitudeAlimentaire(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    jour = models.DateTimeField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    repas = models.CharField(max_length=100)
    boisson = models.CharField(max_length=100)
    lieux = models.CharField(max_length=100)
    
    