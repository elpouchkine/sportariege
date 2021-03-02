from django.db import models

class prestataire(models.Model):
    nomPrestataire = models.CharField(max_length=50, unique=True)
    adressePrestataire = models.CharField(max_length=50)
    telephonePrestataire = models.CharField(max_length=20, unique=True)
    mailPrestataire = models.EmailField(max_length=200, unique=True, primary_key=True)
    
    
    
class typeActivite(models.Model):
    typeActivite = models.CharField(max_length=50, primary_key=True)
    
    def __str__(self):
        return self.typeActivite
    
    
    
    
class client(models.Model):
    nomClient = models.CharField(max_length=50)
    telephoneClient = models.CharField(max_length=20)
    mailClient = models.EmailField(max_length=200, unique=True, primary_key=True)
        

class sorties(models.Model):
    typeActivite = models.ForeignKey(typeActivite, on_delete=models.CASCADE)
    prestataireActivite = models.ForeignKey(prestataire, on_delete=models.CASCADE)
    nomSortie = models.CharField(max_length=50)
    tarifActivite = models.FloatField(null=False)
    rdvActivite = models.CharField(max_length=200)
    thumbnailActivite = models.URLField()
    dateDispo = models.DateField()
    
    class Meta:
        unique_together = (("prestataireActivite", "nomSortie", "dateDispo"))