from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from contracts.models import Contract
from contracts.models import ContractDetails
from clients.models import Client
import datetime
import json

# Create your views here.
def pay(request):

    id = request.GET.get('id')

    contractdetails = get_object_or_404(ContractDetails, pk=id)
    contract = Contract.objects.get(id=contractdetails.contract.id)

    contractdetails.payment = contract.mensualprice
    contractdetails.payment_date = datetime.datetime.today()
    contractdetails.save()

    response = {'retorno': 'Ok'}
    return HttpResponse(json.dumps(response), content_type='application/json')

def payments(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all().order_by('id')
    contractdetails = None
    payments = []
    client = None
    if request.method == 'POST':
        client = request.POST.get('client')

        selected_client = Client.objects.get(name=client)
        try:
            contracts = Contract.objects.filter(client=selected_client.id).order_by('id')
        except:
            contracts = None

        for contract in contracts:
            contractdetails = ContractDetails.objects.filter(contract=contract).order_by('id')
            payments.extend(contractdetails)

       

    
    return render(request, "payments/payments.html", {'clients':clients,'selected_client':client,'payments':payments})

