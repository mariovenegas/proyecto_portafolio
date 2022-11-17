from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Advisory
from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract 
import json

# Create your views here.
def advisorys(request):


    professional = Professional.objects.get(username=request.user.username)
    try:
        advisorys = Advisory.objects.filter(professional=professional.id).order_by('id')
    except:
        advisorys = None

    return render(request, "advisorys/advisorys.html", {'advisorys':advisorys})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    contracts = Contract.objects.all()
    return render(request, 'advisorys/create.html', {'clients':clients, 'contracts':contracts})

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    contract = request.POST.get('contract')
    attendees = request.POST.get('attendees')
    client = request.POST.get('client')
    topic = request.POST.get('topic')
    date = request.POST.get('date')
    professional = Professional.objects.get(username=request.user.username)
    selected_client = Client.objects.get(name=client)

    selected_contract = Contract.objects.get(contract=contract)
    advisory = Advisory(attendees=attendees, client=selected_client, topic=topic, date=date, professional=professional, contract=selected_contract  )
    advisory.save()

    return HttpResponseRedirect('/advisorys/')

def edit(request, advisory_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    
    advisory = get_object_or_404(Advisory, pk=advisory_id)

    selected_client = Client.objects.get(name=advisory.client.name)
    contracts = Contract.objects.filter(client=selected_client)
    return render(request, 'advisorys/edit.html', {'advisory': advisory, 'clients': clients, 'contracts':contracts})

def update(request, advisory_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    advisory = get_object_or_404(Advisory, pk=advisory_id)
    client = Client.objects.get(name=request.POST.get('client'))
    #professional = Professional.objects.get(username=request.user.username)
    contract = Contract.objects.get(contract=request.POST.get('contract'))

    advisory.attendees = request.POST.get('attendees')
    advisory.client = client
    advisory.topic = request.POST.get('topic')
    advisory.date = request.POST.get('date')
    #advisory.professional = professional
    advisory.contract = contract

    advisory.save()
    return HttpResponseRedirect('/advisorys/')

def delete(request, advisory_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    advisory = get_object_or_404(Advisory, pk=advisory_id)
    advisory.delete()
    return HttpResponseRedirect('/advisorys/')

def delete_advisorys(request, advisory_id):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    advisory = get_object_or_404(Advisory, pk=advisory_id)
    
    if request.method == 'POST':
        advisory.delete()
        return HttpResponseRedirect('/advisorys/')
    
    return render(request, 'advisorys/delete_advisorys.html', {'advisory': advisory})

def setstate(request):

    advisory = request.GET.get('advisory')
    state = request.GET.get('state')

    advisory = get_object_or_404(Advisory, pk=advisory)
    advisory.state = state

    advisory.save()

    response = {'resultado': 'ok'}
    return HttpResponse(json.dumps(response), content_type='application/json')