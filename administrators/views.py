from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Administrator

# Create your views here.
def administrators(request):

    administrators = Administrator.objects.all()
    return render(request, "administrators/administrators.html", {'administrators':administrators})

def create(request):
    return render(request, 'administrators/create.html')

def insert(request):
    rut = request.POST.get('rut')
    dv = request.POST.get('dv')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    state = request.POST.get('state')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    administrator = Administrator(rut=rut, dv=dv, name=name, email=email, phone=phone, state=state,username=username,password=password  )
    administrator.save()

    return HttpResponseRedirect('/administrators/')

def edit(request, administrator_id):
    administrator = get_object_or_404(Administrator, pk=administrator_id)
    return render(request, 'administrators/edit.html', {'administrator': administrator})

def update(request, administrator_id):
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

def delete(request, administrator_id):
    administrator = get_object_or_404(Administrator, pk=administrator_id)
    administrator.delete()
    return HttpResponseRedirect('/administrators/')

def delete_administrator(request, administrator_id):
    administrator = get_object_or_404(Administrator, pk=administrator_id)
    
    if request.method == 'POST':
        administrator.delete()
        return HttpResponseRedirect('/administrators/')
    
    return render(request, 'administrators/delete_administrator.html', {'administrator': administrator})