from django.db import models

# Create your models here.
class Clients(models.Model):
    nom = models.CharField('Nom du Client', max_length=120)
    prenom = models.CharField('Prenom du  Client', max_length=120)
    sexe = models.CharField('Sexe', max_length=50)
    adresse = models.CharField('adresse du Client', max_length=120)
    tel = models.CharField('Telephone du Client', max_length=120)
    profession = models.CharField('Profession du Client', max_length=50)

    def __str__(self):
        return self.nom

class Personnels(models.Model):
    nom = models.CharField('Nom du Personnel', max_length=120)
    prenom = models.CharField('Prenom du  Personnel', max_length=120)
    adresse = models.CharField('Adresse du Personnel', max_length=120)
    tel = models.CharField('Telephone du Personnel', max_length=120)
    email = models.EmailField("Email du Personnel", max_length=254)
    statut = models.CharField('Statut du Personnel', max_length=50)
    grade = models.CharField("Grade du Personnel", max_length=50)
    specialite = models.CharField('specialite du Personnel', max_length=50)

    def __str__(self):
        return self.nom

							
class Dossiers(models.Model):

    date = models.DateTimeField("Date de reception")
    statut = models.CharField("Statut du Dossier", max_length=50)
    categorie = models.CharField("Categorie du Dossier", max_length=50)
    description = models.TextField("Description")
    clients = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.statut
