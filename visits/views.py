from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Visit
from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract 

# Create your views here.
def visits(request):

    visits = Visit.objects.all()
    return render(request, "visits/visits.html", {'visits':visits})

def create(request):
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    contracts = Contract.objects.all()
    return render(request, 'visits/create.html', {'clients':clients, 'professionals':professionals, 'contracts':contracts})

def insert(request):
    contract = request.POST.get('contract')
    reason = request.POST.get('reason')
    client = request.POST.get('client')
    date = request.POST.get('date')
    professional = request.POST.get('professional')
    selected_client = Client.objects.get(name=client)
    selected_professional = Professional.objects.get(name=professional)
    selected_contract = Contract.objects.get(contract=contract)
    visit = Visit( client=selected_client, reason=reason,  date=date, professional=selected_professional, contract=selected_contract  )
    visit.save()

    return HttpResponseRedirect('/visits/')

def edit(request, visit_id):
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    contracts = Contract.objects.all()
    visit = get_object_or_404(Visit, pk=visit_id)
    return render(request, 'visits/edit.html', {'visit': visit, 'clients': clients, 'professionals': professionals, 'contracts':contracts})

def update(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    client = Client.objects.get(name=request.POST.get('client'))
    professional = Professional.objects.get(name=request.POST.get('professional'))
    contract = Contract.objects.get(contract=request.POST.get('contract'))

    visit.client = client
    visit.reason = request.POST.get('reason')
    visit.date = request.POST.get('date')
    visit.professional = professional
    visit.contract = contract

    visit.save()
    return HttpResponseRedirect('/visits/')

def delete(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    visit.delete()
    return HttpResponseRedirect('/visits/')

def delete_visits(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    
    if request.method == 'POST':
        visit.delete()
        return HttpResponseRedirect('/visits/')
    
    return render(request, 'visits/delete_visits.html', {'visit': visit})