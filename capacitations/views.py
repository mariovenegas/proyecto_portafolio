from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Capacitation
from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract 

# Create your views here.
def capacitations(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    capacitations = Capacitation.objects.all()
    return render(request, "capacitations/capacitations.html", {'capacitations':capacitations})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    contracts = Contract.objects.all()
    return render(request, 'capacitations/create.html', {'clients':clients, 'professionals':professionals, 'contracts':contracts})

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    attendees = request.POST.get('attendees')
    professional = request.POST.get('professional')
    topic = request.POST.get('topic')
    date = request.POST.get('date')
    client = request.POST.get('client')
    contract = request.POST.get('contract')
    selected_client = Client.objects.get(name=client)
    selected_professional = Professional.objects.get(name=professional)
    selected_contract = Contract.objects.get(contract=contract)
    capacitation = Capacitation(attendees=attendees, professional= selected_professional, topic=topic, date=date, client=selected_client, contract=selected_contract)
    capacitation.save()

    return HttpResponseRedirect('/capacitations/')

def edit(request, capacitation_id):
    if not(request.user.is_authenticated):
        return redirect("index")
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    contracts = Contract.objects.all()
    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    return render(request, 'capacitations/edit.html', {'capacitation': capacitation, 'clients': clients, 'professionals': professionals, 'contracts':contracts})

def update(request, capacitation_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    client = Client.objects.get(name=request.POST.get('client'))
    professional = Professional.objects.get(name=request.POST.get('professional'))
    contract = Contract.objects.get(contract=request.POST.get('contract'))

    capacitation.attendees = request.POST.get('attendees')
    capacitation.topic = request.POST.get('topic')
    capacitation.address = request.POST.get('address')
    capacitation.date = request.POST.get('date')
    capacitation.client = client
    capacitation.professional = professional
    capacitation.contract = contract
    capacitation.save()
    return HttpResponseRedirect('/capacitations/')

def delete(request, capacitation_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    capacitation.delete()
    return HttpResponseRedirect('/capacitations/')

def delete_capacitations(request, capacitation_id):
    if not(request.user.is_authenticated):
        return redirect("index")
    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    
    if request.method == 'POST':
        capacitation.delete()
        return HttpResponseRedirect('/capacitations/')
    
    return render(request, 'capacitations/delete_capacitations.html', {'capacitation': capacitation})