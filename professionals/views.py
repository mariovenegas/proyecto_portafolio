from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Professional

# Create your views here.
def professionals(request):

    professionals = Professional.objects.all()
    return render(request, "professionals/professionals.html", {'professionals':professionals})

def create(request):
    return render(request, 'professionals/create.html')

def insert(request):
    rut = request.POST.get('rut')
    dv = request.POST.get('dv')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    state = request.POST.get('state')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    professional = Professional(rut=rut, dv=dv, name=name, email=email, phone=phone, state=state,username=username,password=password  )
    professional.save()

    return HttpResponseRedirect('/professionals/')

def edit(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    return render(request, 'professionals/edit.html', {'professional': professional})

def update(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)

    professional.rut = request.POST.get('rut')
    professional.dv = request.POST.get('dv')
    professional.name = request.POST.get('name')
    professional.email = request.POST.get('email')
    professional.phone = request.POST.get('phone')
    professional.state = request.POST.get('state')
    professional.username = request.POST.get('username')
    professional.password = request.POST.get('password')
    professional.save()
    return HttpResponseRedirect('/professionals/')

def delete(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    professional.delete()
    return HttpResponseRedirect('/professionals/')

def delete_professional(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    
    if request.method == 'POST':
        professional.delete()
        return HttpResponseRedirect('/professionals/')
    
    return render(request, 'professionals/delete_professional.html', {'professional': professional})