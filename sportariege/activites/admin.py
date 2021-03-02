from django.contrib import admin

# Register your models here.
from activites.models import typeActivite, client, prestataire, sorties


admin.site.register(client)
admin.site.register(prestataire)
admin.site.register(sorties)
admin.site.register(typeActivite)