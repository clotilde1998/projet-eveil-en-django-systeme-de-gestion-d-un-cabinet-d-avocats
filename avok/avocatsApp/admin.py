from django.contrib import admin

from .models import*

admin.site.register(Clients)
admin.site.register(Personnels)
admin.site.register(Dossiers)
admin.site.register(Conseils)
admin.site.register(Audiences)
admin.site.register(Honoraires)

# Register your models here.
