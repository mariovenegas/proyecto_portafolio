from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Advisory
from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract 

# Create your views here.
def advisorys(request):

    advisorys = Advisory.objects.all()
    return render(request, "advisorys/advisorys.html", {'advisorys':advisorys})

def create(request):
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    contracts = Contract.objects.all()
    return render(request, 'advisorys/create.html', {'clients':clients, 'professionals':professionals, 'contracts':contracts})

def insert(request):
    contract = request.POST.get('contract')
    attendees = request.POST.get('attendees')
    client = request.POST.get('client')
    topic = request.POST.get('topic')
    date = request.POST.get('date')
    professional = request.POST.get('professional')
    selected_client = Client.objects.get(name=client)
    selected_professional = Professional.objects.get(name=professional)
    selected_contract = Contract.objects.get(contract=contract)
    advisory = Advisory(attendees=attendees, client=selected_client, topic=topic, date=date, professional=selected_professional, contract=selected_contract  )
    advisory.save()

    return HttpResponseRedirect('/advisorys/')

def edit(request, advisory_id):
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    contracts = Contract.objects.all()
    advisory = get_object_or_404(Advisory, pk=advisory_id)
    return render(request, 'advisorys/edit.html', {'advisory': advisory, 'clients': clients, 'professionals': professionals, 'contracts':contracts})

def update(request, advisory_id):
    advisory = get_object_or_404(Advisory, pk=advisory_id)
    client = Client.objects.get(name=request.POST.get('client'))
    professional = Professional.objects.get(name=request.POST.get('professional'))
    contract = Contract.objects.get(contract=request.POST.get('contract'))

    advisory.attendees = request.POST.get('attendees')
    advisory.client = client
    advisory.topic = request.POST.get('topic')
    advisory.date = request.POST.get('date')
    advisory.professional = professional
    advisory.contract = contract

    advisory.save()
    return HttpResponseRedirect('/advisorys/')

def delete(request, advisory_id):
    advisory = get_object_or_404(Advisory, pk=advisory_id)
    advisory.delete()
    return HttpResponseRedirect('/advisorys/')

def delete_advisorys(request, advisory_id):
    advisory = get_object_or_404(Advisory, pk=advisory_id)
    
    if request.method == 'POST':
        advisory.delete()
        return HttpResponseRedirect('/advisorys/')
    
    return render(request, 'advisorys/delete_advisorys.html', {'advisory': advisory})