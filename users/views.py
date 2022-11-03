from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group

from users.models import UserClient
from regions.models import Region
from communes.models import Commune
from clients.models import Client

# Create your views here.
def users(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    users = UserClient.objects.all()
    return render(request, "users/users.html", {'users':users})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    regions = Region.objects.all()
    clients = Client.objects.all()
    return render(request, 'users/create.html', {'clients':clients, 'regions':regions})


def insert(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    client = request.POST.get('client')
    rut = request.POST.get('rut')
    dv = request.POST.get('dv')
    name = request.POST.get('name')
    address = request.POST.get('address')
    commune = request.POST.get('commune')
    username = request.POST.get('username')
    password = request.POST.get('password')
    selected_client = Client.objects.get(name=client)
    selected_commune = Commune.objects.get(commune=commune)
    
    user = UserClient(rut=rut, dv=dv, name=name, address=address, commune=selected_commune, client=selected_client,username=username,password=password)
    user.save()

    user = User.objects.create_user(username)
    user.is_superuser=0
    user.is_staff=0
    user.is_active=1
    user.save()
    u = User.objects.get(username=username)
    u.set_password(password)
    g = Group.objects.get(name='clientes')
    u.groups.add(g.id)
    u.save()

    return HttpResponseRedirect('/users/')

def edit(request, user_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    regions = Region.objects.all()
    communes = Commune.objects.all()
    clients = Client.objects.all()
    user = get_object_or_404(UserClient, pk=user_id)
    return render(request, 'users/edit.html', {'user': user, 'clients': clients, 'regions': regions, 'communes': communes})

def update(request, user_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    user = get_object_or_404(UserClient, pk=user_id)
    commune = Commune.objects.get(commune=request.POST.get('commune'))
    client = Client.objects.get(name=request.POST.get('client'))

    user.client = client
    user.rut = request.POST.get('rut')
    user.dv = request.POST.get('dv')
    user.name = request.POST.get('name')
    user.address = request.POST.get('address')
    user.commune = commune
    user.username = request.POST.get('username')
    user.password = request.POST.get('password')
    user.save()
    return HttpResponseRedirect('/users/')

def delete_user(request, user_id):

    if not(request.user.is_authenticated):
        return redirect("index")

    user = get_object_or_404(UserClient, pk=user_id)
    
    if request.method == 'POST':

        u = User.objects.get(username=user.username)
        g = Group.objects.get(name='clientes')
        u.groups.remove(g.id)
        u.is_active=0
        u.save()

        user.delete()
        return HttpResponseRedirect('/users/')
    
    return render(request, 'users/delete_user.html', {'user': user})
