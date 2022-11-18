from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Capacitation
from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract 
from django.http import HttpResponse
import json

# Create your views here.
def capacitations(request):


    professional = Professional.objects.get(username=request.user.username)
    try:
        capacitations = Capacitation.objects.filter(professional=professional.id).order_by('id')
    except:
        capacitations = None

    return render(request, "capacitations/capacitations.html", {'capacitations':capacitations})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    contracts = Contract.objects.all()
    return render(request, 'capacitations/create.html', {'clients':clients, 'contracts':contracts})

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    attendees = request.POST.get('attendees')
    topic = request.POST.get('topic')
    date = request.POST.get('date')
    client = request.POST.get('client')
    contract = request.POST.get('contract')
    professional = Professional.objects.get(username=request.user.username)
    selected_client = Client.objects.get(name=client)
    selected_contract = Contract.objects.get(contract=contract)
    capacitation = Capacitation(attendees=attendees, professional=professional, topic=topic, date=date, client=selected_client, contract=selected_contract)
    capacitation.save()

    return HttpResponseRedirect('/capacitations/')

def edit(request, capacitation_id):
    if not(request.user.is_authenticated):
        return redirect("index")
    clients = Client.objects.all()
    contracts = Contract.objects.all()
    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    return render(request, 'capacitations/edit.html', {'capacitation': capacitation, 'clients': clients,  'contracts':contracts})

def update(request, capacitation_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    client = Client.objects.get(name=request.POST.get('client'))
    contract = Contract.objects.get(contract=request.POST.get('contract'))

    capacitation.attendees = request.POST.get('attendees')
    capacitation.topic = request.POST.get('topic')
    capacitation.address = request.POST.get('address')
    capacitation.date = request.POST.get('date')
    capacitation.client = client
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

def setstate(request):

    capacitation = request.GET.get('capacitation')
    state = request.GET.get('state')

    capacitation = get_object_or_404(Capacitation, pk=capacitation)
    capacitation.state = state

    capacitation.save()

    response = {'resultado': 'ok'}
    return HttpResponse(json.dumps(response), content_type='application/json')

def capacitation_review(request):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    capacitations = Capacitation.objects.all()


    return render(request, "capacitations/capacitation_review.html", {'capacitations':capacitations})