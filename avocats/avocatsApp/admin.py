from django.contrib import admin

from .models import Clients, Personnels, Dossiers

admin.site.register(Clients)
admin.site.register(Personnels)
admin.site.register(Dossiers)

# Register your models here.
