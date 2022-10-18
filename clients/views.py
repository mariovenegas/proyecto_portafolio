from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Client

# Create your views here.
def clients(request):

    clients = Client.objects.all()
    return render(request, "clients/clients.html", {'clients':clients})

def create(request):
    return render(request, 'clients/create.html')

def insert(request):
    rut = request.POST.get('rut')
    dv = request.POST.get('dv')
    name = request.POST.get('name')
    sector = request.POST.get('sector')
    address = request.POST.get('address')
    comune = request.POST.get('comune')
    region = request.POST.get('region')
    client = Client(rut=rut, dv=dv, name=name, sector=sector, address=address, comune=comune, region=region )
    client.save()
    return HttpResponseRedirect('/clients/')

def edit(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'clients/edit.html', {'client': client})

def update(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    client.rut = request.POST.get('rut')
    client.dv = request.POST.get('dv')
    client.name = request.POST.get('name')
    client.sector = request.POST.get('sector')
    client.address = request.POST.get('address')
    client.comune = request.POST.get('comune')
    client.region = request.POST.get('region')
    client.save()
    return HttpResponseRedirect('/clients/')

def delete(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return HttpResponseRedirect('/clients/')