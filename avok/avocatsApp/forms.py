from django.forms import ModelForm 
from .models import Clients, Personnels, Dossiers, Conseils, Audiences, Honoraires
from django.db.models import fields 
from django.db import models

class ClientsForm(ModelForm):
    class Meta:
	    model = Clients
	    fields = '__all__'

	    labels = {
		    'Nom': '',  
		    'Prenom': '',    
			'Sexe':'', 
		    'Adresse': '',  
			'numero carte': '',
			'Delivre le': '',
			'Qualite' : '',
		    'Tel': '',
		    'Profession': '', 
	    }
'''
	    #widgets = {
		    #'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom',}),  
		    #'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'prenom',}), 
		    #'adresse': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'adresse',}), 
		    #'tel': form.TextInput(attrs={'class': 'form-select', 'placeholder': 'tel',}),  
		    #'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'profession',}),  
								
	    #}
'''


class PersonnelsForm(ModelForm):
    class Meta:
	    model = Personnels
	    fields = '__all__'

	    labels = {
			
		    'Nom': '',  
		    'Prenom': '', 
		    'Adresse': '',  
		    'Tel': '', 
		    'Email': '',  
            'Domaine': '',
            'Specialite': '',
	    }
'''
	    widgets = {
		    'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom',}),  
		    'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'prenom',}), 
		    'adresse': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'adresse',}), 
		    'tel': form.TextInput(attrs={'class': 'form-select', 'placeholder': 'tel',}),  
		    'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email',}), 
            'statut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'statut',}), 
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'specialite',})				
	    }
'''

class DossiersForm(ModelForm):
    class Meta:
	    model = Dossiers
	    fields ='__all__'

	    labels = {
		    'Date': '',  
		    'Contre': '',  
			'Avocat Adverse' : '',
			'Detail Juridiction': '',
			'Nature':'',
			#'Reclamation':'',
			'Commentaire'
			'Objet':'',
			'Avocat en Charge':'',  
		    'Client': '', 
		    'Personnel': '',  
	    }

class ConseilsForm(ModelForm):
    class Meta:
	    model = Conseils
	    fields ='__all__'

	    labels = {
		    'Date': '',      
		    'Categorie': '',
			'Description':'',  
		    'Client': '', 
		    'Personnel': '',  
	    }

class AudiencesForm(ModelForm):
    class Meta:
	    model = Audiences
	    fields ='__all__'

	    labels = {
		    'Date': '', 
			'Statut': '',
			'Subtitution':'',  
		    'Personne': '',
			'Juridiction':'',
			'Dossier':'',  
		    'Client': '', 
		    'Personnel': '',  
			'Decision':'',
	    }
class HonorairesForm(ModelForm):
    class Meta:
	    model = Honoraires
	    fields ='__all__'

	    labels = {
		    'Date': '',  
		    'Payement': '',    
		    'Total': '',
			'Reste':'',  
			'Montant':'',
		    'Client': '',
			'Dossier': '',
		    'Personnel': '',  
	    }
'''
	    widgets = {
		    'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'date',}),  
		    'statut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'statut',}), 
		    'categorie': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'categorie',}), 
		    'client': form.TextInput(attrs={'class': 'form-select', 'placeholder': 'client',}),  
		    'personnel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'personnel',}),  
								
	    }
'''