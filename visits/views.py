from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Visit
from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract 
from django.http import HttpResponse
import json


# Create your views here.
def visits(request):


    professional = Professional.objects.get(username=request.user.username)
    try:
        visits = Visit.objects.filter(professional=professional.id).order_by('id')
    except:
        visits = None

    return render(request, "visits/visits.html", {'visits':visits})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    contracts = Contract.objects.all()
    return render(request, 'visits/create.html', {'clients':clients, 'contracts':contracts})

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    contract = request.POST.get('contract')
    reason = request.POST.get('reason')
    client = request.POST.get('client')
    date = request.POST.get('date')
    selected_client = Client.objects.get(name=client)
    professional = Professional.objects.get(username=request.user.username)
    selected_contract = Contract.objects.get(contract=contract)
    visit = Visit( client=selected_client, reason=reason,  date=date, professional=professional, contract=selected_contract  )
    visit.save()

    return HttpResponseRedirect('/visits/')

def edit(request, visit_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    contracts = Contract.objects.all()
    visit = get_object_or_404(Visit, pk=visit_id)
    return render(request, 'visits/edit.html', {'visit': visit, 'clients': clients, 'contracts':contracts})

def update(request, visit_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    visit = get_object_or_404(Visit, pk=visit_id)
    client = Client.objects.get(name=request.POST.get('client'))
    contract = Contract.objects.get(contract=request.POST.get('contract'))

    visit.client = client
    visit.reason = request.POST.get('reason')
    visit.date = request.POST.get('date')
    visit.contract = contract

    visit.save()
    return HttpResponseRedirect('/visits/')

def delete(request, visit_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    visit = get_object_or_404(Visit, pk=visit_id)
    visit.delete()
    return HttpResponseRedirect('/visits/')

def delete_visits(request, visit_id):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    visit = get_object_or_404(Visit, pk=visit_id)
    
    if request.method == 'POST':
        visit.delete()
        return HttpResponseRedirect('/visits/')
    
    return render(request, 'visits/delete_visits.html', {'visit': visit})

def setstate(request):

    visit = request.GET.get('visit')
    state = request.GET.get('state')

    visit = get_object_or_404(Visit, pk=visit)
    visit.state = state

    visit.save()

    response = {'resultado': 'ok'}
    return HttpResponse(json.dumps(response), content_type='application/json')

def visit_review(request):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    visits = Visit.objects.all()


    return render(request, "visits/visit_review.html", {'visits':visits})