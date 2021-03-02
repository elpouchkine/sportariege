from django.http import HttpResponse
from activites.models import typeActivite, sorties, client, prestataire
from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(request):
    activite = typeActivite.objects.all().order_by('typeActivite')
    context = {
        'activites': activite
    }
    return render(request, 'administration/index.html', context)

def activites(request):
    activite = typeActivite.objects.all().order_by('typeActivite')
    presta = prestataire.objects.all().order_by('nomPrestataire')
    nomPrestataire = [prestataire.nomPrestataire for prestataire in presta]
        
    if request.method == 'POST':
        nomActivite = request.POST.get('nomActivite')
        typeSortie = request.POST.get('typeActivite')
        presta = request.POST.get('prestataire')
        tarif = request.POST.get('tarif')
        rdv = request.POST.get('rdv')
        lienImg = request.POST.get('lienImg')
        date = request.POST.get('date')
        sortieUnique = sorties.objects.filter(
                prestataireActivite=prestataire, 
                dateDispo=date
            )
        
        if not sortieUnique.exists():
            sortieUnique = sorties.objects.create(
                nomSortie=nomActivite,
                typeActivite=typeSortie,
                prestataireActivite=presta,
                tarifActivite=tarif,
                rdvActivite=rdv,
                thumbnailActivite=lienImg,
                dateDispo=date
            )
            context = {
                'activites': activite,
                'prestataires': nomPrestataire,
                'nomActivite': nomActivite
            }
            return render(request, 'administration/activites.html', context)
        
        else:
            sortie = sortie.first()
            context = {
                'activites': activite,
                'prestataires': nomPrestataire,
                'prestataire': presta,
                'date': date
            }
            return render(request, 'administration/activites.html', context)
        
    else:
        context = {
            'activites': activite,
            'prestataires': nomPrestataire
        }
        return render(request, 'administration/activites.html', context)