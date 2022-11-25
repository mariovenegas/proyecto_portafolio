from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Checklist
from .models import Checklistdetail
from clients.models import Client
from contracts.models import Contract
from services.models import Service

# Create your views here.
def checklists(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    checklists = Checklist.objects.all()
    return render(request, "checklists/checklists.html", {'checklists':checklists})


def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    contracts = Contract.objects.all()
    return render(request, 'checklists/create.html', {'clients':clients, 'contracts':contracts})


def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    client = request.POST.get('client')
    contract = request.POST.get('contract')
    description = request.POST.get('description')
    preguntas = request.POST.getlist('questions[]')
    
    selected_client = Client.objects.get(name=client)
    selected_contract = Contract.objects.get(contract=contract)

    checklist = Checklist(client=selected_client, contract=selected_contract, description=description )
    checklist.save()

    for pregunta in preguntas:
        checklistdetail = Checklistdetail(checklist=checklist, description = pregunta)
        checklistdetail.save()

    return HttpResponseRedirect('/checklists/')


def edit(request, checklist_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    #contracts = Contract.objects.all()
    checklist = get_object_or_404(Checklist, pk=checklist_id)
    checklistdetails = Checklistdetail.objects.filter(checklist=checklist).order_by('id')
    contracts = Contract.objects.filter(client=checklist.client).order_by('id')

    return render(request, 'checklists/edit.html', {'checklist': checklist, 'clients': clients, 'contracts': contracts, 'checklistdetails':checklistdetails})


def update(request, checklist_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    checklist = get_object_or_404(Checklist, pk=checklist_id)
    client = Client.objects.get(name=request.POST.get('client'))
    contract = Contract.objects.get(contract=request.POST.get('contract'))

    preguntas = request.POST.getlist('questions[]')

    checklist.client = client
    checklist.contract = contract
    checklist.description = request.POST.get('description')

    checklist.save()

    Checklistdetail.objects.filter(checklist=checklist).delete()

    for pregunta in preguntas:
        checklistdetail = Checklistdetail(checklist=checklist, description = pregunta)
        checklistdetail.save()

    return HttpResponseRedirect('/checklists/')

def delete(request, contract_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    contract = get_object_or_404(Contract, pk=contract_id)
    contract.delete()
    return HttpResponseRedirect('/checklists/')

def delete_checklists(request, checklist_id):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    checklist = get_object_or_404(Checklist, pk=checklist_id)
    
    
    if request.method == 'POST':
        Checklistdetail.objects.filter(checklist=checklist).delete()
        checklist.delete()
        return HttpResponseRedirect('/checklists/')
    
    return render(request, 'checklists/delete_checklists.html', {'checklist': checklist})

def review(request, checklist_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    clients = Client.objects.all()
    #contracts = Contract.objects.all()
    checklist = get_object_or_404(Checklist, pk=checklist_id)
    checklistdetails = Checklistdetail.objects.filter(checklist=checklist).order_by('id')
    contracts = Contract.objects.filter(client=checklist.client).order_by('id')

    return render(request, 'checklists/review.html', {'checklist': checklist, 'clients': clients, 'contracts': contracts, 'checklistdetails':checklistdetails})


def update_review(request, checklist_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    respuestas = request.POST.getlist('answers[]')
    index = request.POST.getlist('index[]')

    for i, resp in zip(index, respuestas):
        checklistdetail = get_object_or_404(Checklistdetail, pk=i)
        checklistdetail.result=resp
        checklistdetail.save()

    return HttpResponseRedirect('/checklists/')
