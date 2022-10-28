from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Reportaccident

# Create your views here.
def reportaccidents(request):

    reportaccidents = Reportaccident.objects.all()
    return render(request, "reportaccidents/reportaccidents.html", {'reportaccidents':reportaccidents})

def create(request):
    return render(request, 'reportaccidents/create.html')

def insert(request):
    description = request.POST.get('description')
    zone = request.POST.get('zone')
    date = request.POST.get('date')
    hour = request.POST.get('hour')
    
    reportaccident = Reportaccident(description=description, zone=zone, date=date, hour=hour  )
    reportaccident.save()

    return HttpResponseRedirect('/reportaccidents/')

def edit(request, reportaccident_id):
    reportaccident = get_object_or_404(Reportaccident, pk=reportaccident_id)
    return render(request, 'reportaccidents/edit.html', {'reportaccident': reportaccident})

def update(request, reportaccident_id):
    reportaccident = get_object_or_404(Reportaccident, pk=reportaccident_id)

    reportaccident.description = request.POST.get('description')
    reportaccident.zone = request.POST.get('zone')
    reportaccident.date = request.POST.get('date')
    reportaccident.hour = request.POST.get('hour')
    reportaccident.save()
    return HttpResponseRedirect('/reportaccidents/')

def delete(request, reportaccident_id):
    reportaccident = get_object_or_404(Reportaccident, pk=reportaccident_id)
    reportaccident.delete()
    return HttpResponseRedirect('/reportaccidents/')

def delete_reportaccident(request, reportaccident_id):
    reportaccident = get_object_or_404(Reportaccident, pk=reportaccident_id)
    
    if request.method == 'POST':
        reportaccident.delete()
        return HttpResponseRedirect('/reportaccidents/')
    
    return render(request, 'reportaccidents/delete_reportaccident.html', {'reportaccident': reportaccident})