from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Contract
from clients.models import Client
from services.models import Service
import json

# Create your views here.
def contracts(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    contracts = Contract.objects.all()
    return render(request, "contracts/contracts.html", {'contracts':contracts})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    services = Service.objects.all()
    return render(request, 'contracts/create.html', {'clients':clients, 'services':services})

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    contract = request.POST.get('contract')
    client = request.POST.get('client')
    description = request.POST.get('description')
    datestart = request.POST.get('datestart')
    dateend = request.POST.get('dateend')
    service = request.POST.get('service')
    selected_client = Client.objects.get(name=client)
    selected_service = Service.objects.get(service=service)
    contract = Contract(contract=contract, client=selected_client, description=description, datestart=datestart, dateend=dateend, service=selected_service  )
    contract.save()

    return HttpResponseRedirect('/contracts/')

def edit(request, contract_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    services = Service.objects.all()
    contract = get_object_or_404(Contract, pk=contract_id)
    return render(request, 'contracts/edit.html', {'contract': contract, 'clients': clients, 'services': services})

def update(request, contract_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    contract = get_object_or_404(Contract, pk=contract_id)
    client = Client.objects.get(name=request.POST.get('client'))
    service = Service.objects.get(service=request.POST.get('service'))

    contract.contract = request.POST.get('contract')
    contract.description = request.POST.get('description')
    contract.datestart = request.POST.get('datestart')
    contract.dateend = request.POST.get('dateend')
    contract.service = service
    contract.client = client

    contract.save()
    return HttpResponseRedirect('/contracts/')

def delete(request, contract_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    contract = get_object_or_404(Contract, pk=contract_id)
    contract.delete()
    return HttpResponseRedirect('/contracts/')

def delete_contracts(request, contract_id):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    contract = get_object_or_404(Contract, pk=contract_id)
    
    if request.method == 'POST':
        contract.delete()
        return HttpResponseRedirect('/contracts/')
    
    return render(request, 'contracts/delete_contracts.html', {'contract': contract})

def getcontracts(request):

    client_name = request.GET.get('client_name')
    print ("ajax client_name "+ str(client_name))

    selected_client = Client.objects.filter(name=client_name) # retorna un query set

    #print (" region id "+ str(selected_region.region))


    contracts = list(Contract.objects.filter(client__in=selected_client).values('contract'))
    #print "selected selected_region ", selected_region
    #all_communes = selected_region.commune_set.all()
    response = {'contracts': contracts}
    return HttpResponse(json.dumps(response), content_type='application/json')