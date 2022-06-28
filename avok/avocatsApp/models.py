from django.db import models

GENDER = (
			('F', 'Feminin'),
			('M', 'Masculin'),
		)
ARRONDISSEMENT = (
    ('1er Arrondissement', '1er Arrondissemnt'),
    ('2eme Arrondissement', '2eme Arrondissemnt'),
    ('3eme Arrondissement', '3eme Arrondissemnt'),
    ('4eme Arrondissement', '4eme Arrondissemnt'),
    ('5eme Arrondissement', '5eme Arrondissemnt'),
    ('6eme Arrondissement', '6eme Arrondissemnt'),
    ('7eme Arrondissement', '7eme Arrondissemnt'),
    ('8eme Arrondissement', '8eme Arrondissemnt'),
    ('9eme Arrondissement', '9eme Arrondissemnt'),
    ('10eme Arrondissement', '10eme Arrondissemnt'),
)

QUALITE = (
    ('Demandeur', 'Demandeur'),
    ('Defendeur', 'Defendeur'),
    ('Appelant', 'Appelant'),
    ('Intimé', 'Intimé'),
    ('Demandeur au pourvoir', 'Demandeur au pourvoir'),
    ('Defenseur au pourvoir', 'Defenseur au pourvoir'),
    ('Prevenu', 'Prevenu'),
    ('Partie Civile', 'Partie civile'),
    ('Civilement Responsable', 'Civilement Responsable'),
    ('Mise en cause', 'Mise en cause'),
    ('Intervenant', 'Intervenant'),
        )

# Create your models here.
class Clients(models.Model):
    nom = models.CharField('Societe', max_length=120)
    prenom = models.CharField('Prenom du Client', max_length=50)
    sexe = models.CharField(choices=GENDER, null=True, max_length=10)
    adresse = models.CharField(choices=ARRONDISSEMENT, null=True, max_length=20)
    number = models.CharField('Carte d_identite', max_length=50)
    delivrate = models.CharField('Delivre le', max_length=150)
    qualite = models.CharField(choices=QUALITE, null=True, max_length=150)
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
    domaine = models.CharField('domaine du Personnel', max_length=150)
    specialite = models.CharField('specialite du Personnel', max_length=50)

    def __str__(self):
        return self.nom

        
JURIDICTION = (

			('NDjamena', 'NDjamena'),
			('Bongor', 'Bongor'),
            ('Kelo', 'Kelo'),
            ('Moundou', 'Moundou'),
            ('Doba', 'Doba'),
            ('Koumra', 'Koumra'),
            ('Sarh', 'Sarh'),
            ('Amtiman', 'Amtiman'),
            ('Mongo', 'Mongo'),
            ('Lai', 'Lai'),
            ('Pala', 'Pala'),
            ('Abeche', 'Abeche'),
		)   
'''DETAIL = (
            ('Cours Appel','Cours Appel'),
            ('Tribunal Grande Instance', 'Tribunal Grande Instance'),
            ('Tribunal de Commerce', 'Tribunal de Commerce'),
            ('Tribunal de Travail et de Securite Social', 'Tribunal de Travail et de Securite Social'),
            ('Chambre Administratif','Chambre Administratif'),
            ('Tribunal Correctionnel', 'Tribunal Correctionnel'),
            ('Tribunal Presidentiel', 'Tribunal Presidentiel'),

        )	'''
'''NATURE = (
            ('Civile', 'Civile'),
            ('Criminelle', 'Criminelle'),
            ('Commerciale', 'Commerciale'),
            ('Administrative', 'Administrative'),
            ('Correctionnelle', 'Correctionnelle'),
            ('Refere', 'Refere'),
            ('Social','Social'),
            ('Foncier', 'Foncier'),
        )
'''
AVOCAT = (
            ('Me TOG', 'Me TOG'),
            ('Me Clotilde', 'Me Clotilde'),
            ('Me MOUSSA', 'Me MOUSSA'),
)				
class Dossiers(models.Model):

    date = models.DateTimeField("Date de reception")
    contre= models.CharField('Contre', max_length=50)
    avocat_adverse= models.CharField('Avocat Adverse', max_length=50)
    detail_juridiction = models.CharField('Juridiction' , max_length=50)
    nature = models.CharField('Nature', max_length=150)
    #reclamation = models.CharField('Reclamation', max_length=50)
    commentaire = models.TextField('Reclamation' , max_length=50)
    objet = models.CharField("Objet", max_length=50)
    avocat = models.CharField(choices = AVOCAT, null=True, max_length=50)
    clients = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.objet

class Conseils(models.Model):
    
    date = models.DateTimeField("Date de reception")
    categorie = models.CharField("Categorie du Conseil", max_length=50)
    description = models.TextField("Description du Conseil")
    clients = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.categorie

class Audiences(models.Model):
    
    date = models.DateTimeField("Date d'audience")
    statut = models.CharField("Statut", max_length=40)
    subtitution = models.CharField("Subtitution", max_length=50)
    personne = models.CharField("Chambre en Charge", max_length=50)
    juridiction = models.CharField("Juridiction", max_length=50)
    dossiers_audience1 = models.ForeignKey(Dossiers, blank=False, on_delete=models.CASCADE)
    clients_audience1 = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels_audience = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    commentaire = models.CharField('Decisions', max_length=150)
    def __str__(self):
        return self.statut

PAYEMENT = (
			('Cheque', 'Cheque'),
			('Virement', 'Virement'),
            ('Cash', 'Cash'),
		) 

class Honoraires(models.Model):
    
    date = models.DateTimeField("Date de reception")
    payement = models.CharField(choices=PAYEMENT, null=True, max_length=20)
    total = models.PositiveIntegerField("Total")
    reste = models.PositiveIntegerField(" Reste")
    montant = models.PositiveIntegerField("Montant")
    dossierss = models.ForeignKey(Dossiers, blank=False, on_delete=models.CASCADE)
    clientss = models.ForeignKey(Clients, blank=False, on_delete=models.CASCADE)
    personnels01 = models.ForeignKey(Personnels, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.montant