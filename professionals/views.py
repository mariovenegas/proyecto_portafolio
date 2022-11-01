from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group

from .models import Professional

# Create your views here.
def professionals(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    professionals = Professional.objects.all()
    return render(request, "professionals/professionals.html", {'professionals':professionals})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    return render(request, 'professionals/create.html')

def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

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

    user = User.objects.create_user(username)
    user.is_superuser=0
    user.is_staff=0
    user.is_active=1
    user.save()
    u = User.objects.get(username=username)
    u.set_password(password)
    g = Group.objects.get(name='profesionales')
    u.groups.add(g.id)
    u.save()


    return HttpResponseRedirect('/professionals/')

def edit(request, professional_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    professional = get_object_or_404(Professional, pk=professional_id)
    return render(request, 'professionals/edit.html', {'professional': professional})

def update(request, professional_id):
    if not(request.user.is_authenticated):
        return redirect("index")

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


def delete_professional(request, professional_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    professional = get_object_or_404(Professional, pk=professional_id)
    
    if request.method == 'POST':

        u = User.objects.get(username=professional.username)
        g = Group.objects.get(name='profesionales')
        u.groups.remove(g.id)
        u.is_active=0
        u.save()

        professional.delete()
        return HttpResponseRedirect('/professionals/')
    
    return render(request, 'professionals/delete_professional.html', {'professional': professional})