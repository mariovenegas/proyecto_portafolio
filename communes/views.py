from django.shortcuts import render
from django.http import HttpResponse
from .models import Commune
from regions.models import Region
import json
# Create your views here.

def getcommunes(request):

    region_name = request.GET.get('region_name')
    print ("ajax region_name "+ str(region_name))

    selected_region = Region.objects.filter(region=region_name) # retorna un query set

    #print (" region id "+ str(selected_region.region))


    communes = list(Commune.objects.filter(region__in=selected_region).values('commune'))
    #print "selected selected_region ", selected_region
    #all_communes = selected_region.commune_set.all()
    response = {'communes': communes}
    return HttpResponse(json.dumps(response), content_type='application/json')