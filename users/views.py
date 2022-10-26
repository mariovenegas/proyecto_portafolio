from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.
def users(request):

    users = User.objects.all()
    return render(request, "users/users.html", {'users':users})

def create(request):
    return render(request, 'users/create.html')

def insert(request):
    rut = request.POST.get('rut')
    dv = request.POST.get('dv')
    name = request.POST.get('name')
    address = request.POST.get('address')
    commune = request.POST.get('comune')
    type = request.POST.get('type')
    id_client = request.POST.get('id_client')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = User(rut=rut, dv=dv, name=name, address=address, commune=commune, type=type, id_client=id_client,username=username,password=password  )
    user.save()

    return HttpResponseRedirect('/users/')

def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/edit.html', {'user': user})

def update(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    user.rut = request.POST.get('rut')
    user.dv = request.POST.get('dv')
    user.name = request.POST.get('name')
    user.address = request.POST.get('address')
    user.commune = request.POST.get('comune')
    user.type = request.POST.get('type')
    user.id_client = request.POST.get('id_client')
    user.username = request.POST.get('username')
    user.password = request.POST.get('password')
    user.save()
    return HttpResponseRedirect('/users/')

def delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return HttpResponseRedirect('/users/')
