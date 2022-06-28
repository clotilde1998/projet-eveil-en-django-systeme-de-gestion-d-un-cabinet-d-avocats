from django.shortcuts import render, redirect
from .models import Personnels, Clients, Dossiers, Conseils, Audiences, Honoraires
from django.http import HttpResponseRedirect
from .forms import ClientsForm, PersonnelsForm, DossiersForm, ConseilsForm, AudiencesForm, HonorairesForm

def home(request):
	return render(request, 'avocat/home.html', {})

def apropos(request):
    	return render(request, 'avocat/apropos.html', {})

def personnels_list(request):
    personnel = Personnels.objects.all().order_by('nom')
    return render(request, 'avocat/personnels_list.html', {
        'personnels': personnel,
    })



def clients_list(request):
    client = Clients.objects.all().order_by('nom')
    return render(request, 'avocat/clients_list.html', {
        'clients': client,
    })


def dossiers_list(request):
    dossier = Dossiers.objects.all().order_by('objet')
    return render(request, 'avocat/dossiers_list.html', {
        'dossiers': dossier,
    })

def conseils_list(request):
    conseil = Conseils.objects.all().order_by('categorie')
    return render(request, 'avocat/conseils_list.html', {
        'conseils': conseil,
    })

def audience_list(request):
    audience = Audiences.objects.all().order_by('statut')
    return render(request, 'avocat/audience_list.html', {
        'audiences': audience,
    })

def honoraire_list(request):
    honoraire = Honoraires.objects.all().order_by('montant')
    return render(request, 'avocat/honoraire_list.html', {
        'honoraires': honoraire,
    })



def client_add(request):
    submitted = False
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/client_add?submitted=True')
    else:
        form = ClientsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/client_add.html', {
	    'form': form,
	    'submitted': submitted,
})

def personnel_add(request):
    submitted = False
    if request.method == "POST":
        form = PersonnelsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/personnel_add?submitted=True')
    else:
        form = PersonnelsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/personnel_add.html', {
	    'form': form,
	    'submitted': submitted,
})

def dossier_add(request):
    submitted = False
    if request.method == "POST":
        form = DossiersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dossier_add?submitted=True')
    else:
        form = DossiersForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/dossier_add.html', {
		'form': form,
		'submitted': submitted,
})

def conseil_add(request):
    submitted = False
    if request.method == "POST":
        form = ConseilsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/conseil_add?submitted=True')
    else:
        form = ConseilsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/conseil_add.html', {
		'form': form,
		'submitted': submitted,
})

def audience_add(request):
    submitted = False
    if request.method == "POST":
        form = AudiencesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/audience_add?submitted=True')
    else:
        form = AudiencesForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/audience_add.html', {
		'form': form,
		'submitted': submitted,
})

def honoraire_add(request):
    submitted = False
    if request.method == "POST":
        form = HonorairesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/honoraire_add?submitted=True')
    else:
        form = HonorairesForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/honoraire_add.html', {
		'form': form,
		'submitted': submitted,
})

def client_update(request, pk):
    client = Clients.objects.get(nom=pk)
    form = ClientsForm(instance=client)
    if request.method=='POST':
        form = ClientsForm(request.POST,instance=client)
    if form.is_valid():
            form.save()
            return redirect('client-list')
    context={'form':form}
    return render(request, 'avocat/client_add.html', context)

def personnel_update(request, pk):
    personnel = Personnels.objects.get(nom=pk)
    form = PersonnelsForm(instance=personnel)
    if request.method=='POST':
        form = PersonnelsForm(request.POST,instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('personnel-list')
    context={'form':form}
    return render(request, 'avocat/personnel_add.html', context)

'''def dossier_update(request, pk):
    dossier = Dossiers.objects.get(objet=pk)
    form = DossiersForm(instance=dossier)
    if request.method=='POST':
        form = DossiersForm(request.POST,instance=dossier)
    if form.is_valid():
            form.save()
            return redirect('dossier-list')
    context={'form':form}
    return render(request, 'avocat/dossier_add.html', context)

'''
def dossier_update(request, pk):
    dossier = Dossiers.objects.get(nature=pk)
    form = DossiersForm(instance=dossier)
    if request.method=='POST':
        form = DossiersForm(request.POST,instance=dossier)
    if form.is_valid():
            form.save()
            return redirect('dossier-list')
    context={'form':form}
    return render(request, 'avocat/dossier_add.html', context)

def conseil_update(request, pk):
    conseil = Conseils.objects.get(categorie=pk)
    form = ConseilsForm(instance=conseil)
    if request.method=='POST':
        form = ConseilsForm(request.POST,instance=conseil)
    if form.is_valid():
            form.save()
            return redirect('conseils-list')
    context={'form':form}
    return render(request, 'avocat/conseil_add.html', context)

def audience_update(request, pk):
    audience = Audiences.objects.get(statut=pk)
    form = AudiencesForm(instance=audience)
    if request.method=='POST':
        form = AudiencesForm(request.POST,instance=audience)
    if form.is_valid():
            form.save()
            return redirect('audience-list')
    context={'form':form}
    return render(request, 'avocat/audience_add.html', context)

def honoraire_update(request, pk):
    honoraire = Honoraires.objects.get(total=pk)
    form = HonorairesForm(instance=honoraire)
    if request.method=='POST':
        form = HonorairesForm(request.POST,instance=honoraire)
    if form.is_valid():
            form.save()
            return redirect('honoraire-list')
    context={'form':form}
    return render(request, 'avocat/honoraire_add.html', context)

    
def client_delete(request, pk):
    client = Clients.objects.get(nom=pk)
    client.delete()
    return redirect('client-list')

def personnel_delete(request, pk):
    personnel = Personnels.objects.get(nom=pk)
    personnel.delete()
    return redirect('personnel-list')

def dossier_delete(request, pk):
    dossier = Dossiers.objects.get(objet=pk)
    dossier.delete()
    return redirect('dossier-list')

def conseil_delete(request, pk):
    conseil = Conseils.objects.get(categorie=pk)
    conseil.delete()
    return redirect('conseil-list')

def audience_delete(request, pk):
    audience = Audiences.objects.get(statut=pk)
    audience.delete()
    return redirect('audience-list')

def honoraire_delete(request, pk):
    honoraire = Honoraires.objects.get(montant=pk)
    honoraire.delete()
    return redirect('honoraire-list')


