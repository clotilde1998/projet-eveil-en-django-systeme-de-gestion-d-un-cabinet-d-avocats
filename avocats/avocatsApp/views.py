from django.shortcuts import render, redirect
from .models import Personnels, Clients, Dossiers, Conseils, Redactions
from django.http import HttpResponseRedirect
from .forms import ClientsForm, PersonnelsForm, DossiersForm, ConseilsForm, RedactionsForm

def home(request):
	return render(request, 'avocat/home.html', {})


def personnels_list(request):
    personnel = Personnels.objects.all().order_by('nom')
    return render(request, 'avocat/personnels_list.html', {
        'personnel': personnel,
    })



def clients_list(request):
    client = Clients.objects.all().order_by('nom')
    return render(request, 'avocat/clients_list.html', {
        'client': client,
    })


def dossiers_list(request):
    dossiers = Dossiers.objects.all().order_by('statut')
    return render(request, 'avocat/dossiers_list.html', {
        'dossiers': dossiers,
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

def client_update(request, client_id):
    client = Clients.objects.get(pk=client_id)
    form = ClientsForm(request.POST or None, instance=Clients)
    if form.is_valid():
            form.save()
            return redirect('client-list')
    return render(request, 'avocat/client_update.html', {
        'client': client,
        'form': form,
}) 	

def client_delete(request, client_id):
    client = Clients.objects.get(pk=client_id)
    client.delete()
    return redirect('client-list')
    

def conseils_list(request):
    conseil = Conseils.objects.all().order_by('categorie')
    return render(request, 'avocat/conseils_list.html', {
        'conseil': conseil,
    })

def redactions_list(request):
    redaction = Redactions.objects.all().order_by('categorie')
    return render(request, 'avocat/redactions_list.html', {
        'redaction': redaction,
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

def redactions_add(request):
    submitted = False
    if request.method == "POST":
        form = RedactionsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/redactions_add?submitted=True')
    else:
        form = RedactionsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'avocat/redactions_add.html', {
		'form': form,
		'submitted': submitted,
})
# Create your views here.
