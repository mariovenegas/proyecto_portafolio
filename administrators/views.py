from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from .models import Administrator

# Create your views here.
def administrators(request):
    if not(request.user.is_authenticated):
        return redirect("index")

    administrators = Administrator.objects.all()
    return render(request, "administrators/administrators.html", {'administrators':administrators})

def create(request):
    if not(request.user.is_authenticated):
        return redirect("index")
    return render(request, 'administrators/create.html')

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
    

    try:
        user = User.objects.create_user(username)
        user.is_superuser=0
        user.is_staff=0
        user.is_active=1
        user.save()
        u = User.objects.get(username=username)
        u.set_password(password)
        g = Group.objects.get(name='administradores')
        u.groups.add(g.id)
        u.save()
        administrator = Administrator(rut=rut, dv=dv, name=name, email=email, phone=phone, state=state,username=username,password=password  )
        administrator.save()
    except:
        print('Error al crear usuario ' + username)


    return HttpResponseRedirect('/administrators/')

def edit(request, administrator_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    administrator = get_object_or_404(Administrator, pk=administrator_id)
    return render(request, 'administrators/edit.html', {'administrator': administrator})

def update(request, administrator_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    administrator = get_object_or_404(Administrator, pk=administrator_id)

    administrator.rut = request.POST.get('rut')
    administrator.dv = request.POST.get('dv')
    administrator.name = request.POST.get('name')
    administrator.email = request.POST.get('email')
    administrator.phone = request.POST.get('phone')
    administrator.state = request.POST.get('state')
    administrator.username = request.POST.get('username')
    administrator.password = request.POST.get('password')
    administrator.save()
    return HttpResponseRedirect('/administrators/')


def delete_administrator(request, administrator_id):
    if not(request.user.is_authenticated):
        return redirect("index")

    administrator = get_object_or_404(Administrator, pk=administrator_id)
    
    if request.method == 'POST':
        try:
            u = User.objects.get(username=administrator.username)
            g = Group.objects.get(name='administradores')
            u.groups.remove(g.id)
            u.is_active=0
            u.save()
        except:
            print('Error al borrar usuario '+administrator.username)
        
        administrator.delete()
        return HttpResponseRedirect('/administrators/')
    
    return render(request, 'administrators/delete_administrator.html', {'administrator': administrator})