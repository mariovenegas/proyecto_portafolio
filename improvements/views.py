from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Improvement

# Create your views here.
def improvements(request):

    improvements = Improvement.objects.all()
    return render(request, "improvements/improvements.html", {'improvements':improvements})

def create(request):
    return render(request, 'improvements/create.html')

def insert(request):
    case = request.POST.get('case')
    client = request.POST.get('client')
    action = request.POST.get('action')
    professional = request.POST.get('professional')
    
    improvement = Improvement(case=case, client=client, action=action, professional=professional  )
    improvement.save()

    return HttpResponseRedirect('/improvements/')

def edit(request, improvement_id):
    improvement = get_object_or_404(Improvement, pk=improvement_id)
    return render(request, 'improvements/edit.html', {'improvement': improvement})

def update(request, improvement_id):
    improvement = get_object_or_404(Improvement, pk=improvement_id)

    improvement.case = request.POST.get('case')
    improvement.client = request.POST.get('client')
    improvement.action = request.POST.get('action')
    improvement.professional = request.POST.get('professional')
    improvement.save()
    return HttpResponseRedirect('/improvements/')

def delete(request, improvement_id):
    improvement = get_object_or_404(Improvement, pk=improvement_id)
    improvement.delete()
    return HttpResponseRedirect('/improvements/')

def delete_improvements(request, improvement_id):
    improvement = get_object_or_404(Improvement, pk=improvement_id)
    
    if request.method == 'POST':
        improvement.delete()
        return HttpResponseRedirect('/improvements/')
    
    return render(request, 'improvements/delete_improvements.html', {'improvement': improvement})