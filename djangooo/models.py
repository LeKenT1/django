from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    mail = models.EmailField(max_length=254)
    date_naissance = models.DateField()
    lieu = models.CharField(max_length=100)
    adresse_rue = models.CharField(max_length=255)
    adresse_ville = models.CharField(max_length=100)    

    def __str__(self):
        return f"{self.nom} {self.prenom}"
