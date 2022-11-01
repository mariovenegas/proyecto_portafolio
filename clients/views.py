from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import Client
from regions.models import Region
from communes.models import Commune

# Create your views here.
def clients(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()

    return render(request, "clients/clients.html", {'clients':clients})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    regions = Region.objects.all()
    return render(request, 'clients/create.html', {'regions':regions})

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    rut = request.POST.get('rut')
    dv = request.POST.get('dv')
    name = request.POST.get('name')
    sector = request.POST.get('sector')
    address = request.POST.get('address')
    commune = request.POST.get('commune')

    selected_commune = Commune.objects.get(commune=commune)

    client = Client(rut=rut, dv=dv, name=name, sector=sector, address=address, commune=selected_commune )
    client.save() 

    return HttpResponseRedirect('/clients/')

def edit(request, client_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    regions = Region.objects.all()
    communes = Commune.objects.all()
    client = get_object_or_404(Client, pk=client_id)
    #commune = Commune.objects.get(commune=client.commune.commune)
    #region = Region.objects.get(region=commune.region.region)
    region = client.commune.region
    return render(request, 'clients/edit.html', {'client': client, 'region':region, 'regions':regions, 'communes':communes})

def update(request, client_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    client = get_object_or_404(Client, pk=client_id)
    commune = Commune.objects.get(commune=request.POST.get('commune'))

    client.rut = request.POST.get('rut')
    client.dv = request.POST.get('dv')
    client.name = request.POST.get('name')
    client.sector = request.POST.get('sector')
    client.address = request.POST.get('address')
    client.commune = commune

    client.save()
    return HttpResponseRedirect('/clients/')



def delete_client(request, client_id):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    client = get_object_or_404(Client, pk=client_id)
    
    if request.method == 'POST':
        client.delete()
        return HttpResponseRedirect('/clients/')
    
    return render(request, 'clients/delete_client.html', {'client': client})