from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Contract
from clients.models import Client
from services.models import Service
# Create your views here.
def contracts(request):

    contracts = Contract.objects.all()
    return render(request, "contracts/contracts.html", {'contracts':contracts})

def create(request):
    clients = Client.objects.all()
    services = Service.objects.all()
    return render(request, 'contracts/create.html', {'clients':clients, 'services':services})

def insert(request):
    numbercontract = request.POST.get('numbercontract')
    client = request.POST.get('client')
    description = request.POST.get('description')
    datestart = request.POST.get('datestart')
    dateend = request.POST.get('dateend')
    service = request.POST.get('service')
    selected_client = Client.objects.get(name=client)
    selected_service = Service.objects.get(service=service)
    contract = Contract(numbercontract=numbercontract, client=selected_client, description=description, datestart=datestart, dateend=dateend, service=selected_service  )
    contract.save()

    return HttpResponseRedirect('/contracts/')

def edit(request, contract_id):
    clients = Client.objects.all()
    services = Service.objects.all()
    contract = get_object_or_404(Contract, pk=contract_id)
    return render(request, 'contracts/edit.html', {'contract': contract, 'clients': clients, 'services': services})

def update(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    client = Client.objects.get(name=request.POST.get('client'))
    service = Service.objects.get(service=request.POST.get('service'))

    contract.numbercontract = request.POST.get('numbercontract')
    contract.description = request.POST.get('description')
    contract.datestart = request.POST.get('datestart')
    contract.dateend = request.POST.get('dateend')
    contract.service = service
    contract.client = client

    contract.save()
    return HttpResponseRedirect('/contracts/')

def delete(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    contract.delete()
    return HttpResponseRedirect('/contracts/')

def delete_contracts(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    
    if request.method == 'POST':
        contract.delete()
        return HttpResponseRedirect('/contracts/')
    
    return render(request, 'contracts/delete_contracts.html', {'contract': contract})