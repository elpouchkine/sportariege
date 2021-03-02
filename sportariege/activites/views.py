#from django.shortcuts import render

from django.http import HttpResponse
from .models import typeActivite, sorties, client, prestataire
from django.template import loader
from django.shortcuts import render


def index(request):
    activite = typeActivite.objects.all().order_by('typeActivite')
    context = {
        'activites': activite
    }
    return render(request, 'activites/index.html', context)

def activites(request):
    activites = typeActivite.objects.all().order_by('typeActivite')
    context = {
        'activites': activites
    }
    return render(request, 'activites/activites.html', context)

def activite(request, Activite):
    activite = typeActivite.objects.get(pk=Activite)
    activites = typeActivite.objects.all().order_by('typeActivite')
    context = {
        'activite': activite,
        'activites': activites
    }
    
    return render(request, 'activites/activite.html', context)