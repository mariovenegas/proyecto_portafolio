from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Advisory
from clients.models import Client
from professionals.models import Professional
# Create your views here.
def advisorys(request):

    advisorys = Advisory.objects.all()
    return render(request, "advisorys/advisorys.html", {'advisorys':advisorys})

def create(request):
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    return render(request, 'advisorys/create.html', {'clients':clients, 'professionals':professionals})

def insert(request):
    attendees = request.POST.get('attendees')
    client = request.POST.get('client')
    topic = request.POST.get('topic')
    date = request.POST.get('date')
    professional = request.POST.get('professional')
    selected_client = Client.objects.get(name=client)
    selected_professional = Professional.objects.get(name=professional)
    advisory = Advisory(attendees=attendees, client=selected_client, topic=topic, date=date, professional=selected_professional  )
    advisory.save()

    return HttpResponseRedirect('/advisorys/')

def edit(request, advisory_id):
    clients = Client.objects.all()
    professionals = Professional.objects.all()
    advisory = get_object_or_404(Advisory, pk=advisory_id)
    return render(request, 'advisorys/edit.html', {'advisory': advisory, 'clients': clients, 'professionals': professionals})

def update(request, advisory_id):
    advisory = get_object_or_404(Advisory, pk=advisory_id)
    client = Client.objects.get(name=request.POST.get('client'))
    professional = Professional.objects.get(name=request.POST.get('professional'))

    advisory.attendees = request.POST.get('attendees')
    advisory.client = client
    advisory.topic = request.POST.get('topic')
    advisory.date = request.POST.get('date')
    advisory.professional = professional

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