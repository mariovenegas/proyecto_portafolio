from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Capacitation

# Create your views here.
def capacitations(request):

    capacitations = Capacitation.objects.all()
    return render(request, "capacitations/capacitations.html", {'capacitations':capacitations})

def create(request):
    return render(request, 'capacitations/create.html')

def insert(request):
    attendees = request.POST.get('attendees')
    professional = request.POST.get('professional')
    topic = request.POST.get('topic')
    date = request.POST.get('date')
    id_client = request.POST.get('id_client')
    id_contract = request.POST.get('id_contract')
    
    capacitation = Capacitation(attendees=attendees, professional=professional, topic=topic, date=date, id_client=id_client, id_contract=id_contract)
    capacitation.save()

    return HttpResponseRedirect('/capacitations/')

def edit(request, capacitation_id):
    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    return render(request, 'capacitations/edit.html', {'capacitation': capacitation})

def update(request, capacitation_id):
    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)

    capacitation.attendees = request.POST.get('attendees')
    capacitation.professional = request.POST.get('professional')
    capacitation.topic = request.POST.get('topic')
    capacitation.address = request.POST.get('address')
    capacitation.date = request.POST.get('date')
    capacitation.id_client = request.POST.get('id_client')
    capacitation.id_contract = request.POST.get('id_contract')
    capacitation.save()
    return HttpResponseRedirect('/capacitations/')

def delete(request, capacitation_id):
    capacitation = get_object_or_404(Capacitation, pk=capacitation_id)
    capacitation.delete()
    return HttpResponseRedirect('/capacitations/')
