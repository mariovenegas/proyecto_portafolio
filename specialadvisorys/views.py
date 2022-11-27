from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from users.models import UserClient
from clients.models import Client
from .models import Specialadvisory
import json

# Create your views here.
def specialadvisorys(request):

    print(request.user.username)
    try:
        user = UserClient.objects.get(username=request.user.username)
    except:
        user = None
    
    try:
        specialadvisorys = Specialadvisory.objects.filter(user=user.id).order_by('id')
    except:
        specialadvisorys = None




    return render(request, "specialadvisorys/specialadvisorys.html", {'specialadvisorys':specialadvisorys})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    return render(request, 'specialadvisorys/create.html')

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    motive = request.POST.get('motive')
    description = request.POST.get('description')
    date = request.POST.get('date')
    user = UserClient.objects.get(username=request.user.username)
    
    specialadvisory = Specialadvisory(motive=motive, description=description, date=date, user=user )
    specialadvisory.save()

    return HttpResponseRedirect('/specialadvisorys/')

def edit(request, specialadvisory_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    specialadvisory = get_object_or_404(Specialadvisory, pk=specialadvisory_id)
    return render(request, 'specialadvisorys/edit.html', {'specialadvisory': specialadvisory})

def update(request, specialadvisory_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    specialadvisory = get_object_or_404(Specialadvisory, pk=specialadvisory_id)

    specialadvisory.motive = request.POST.get('motive')
    specialadvisory.description = request.POST.get('description')
    specialadvisory.date = request.POST.get('date')
    return HttpResponseRedirect('/specialadvisorys/')


def delete_specialadvisorys(request, advisory_id):
    if not(request.user.is_authenticated):
        return redirect("index")
        
    specialadvisory = get_object_or_404(Specialadvisory, pk=specialadvisory_id)
    
    if request.method == 'POST':
        specialadvisory.delete()
        return HttpResponseRedirect('/specialadvisory/')
    
    return render(request, 'specialadvisory/delete_specialadvisory.html', {'specialadvisory': specialadvisory})