from django.shortcuts import render,redirect
from .models import Dojo,Ninja
def index(request):
    context = {
        'all_ninjas' : Ninja.objects.all(),
        'all_dojos' : Dojo.objects.all(),
    }
    return render(request,'index.html',context)

def add_dojo(request):
    Dojo.objects.create(name = request.POST['dojo_name'],city = request.POST['dojo_city'],state = request.POST['dojo_state'])
    return redirect('/')

def add_ninja(request):
    Ninja.objects.create(dojo = Dojo.objects.get(id = request.POST['dojo']),first_name = request.POST['first_name'],last_name = request.POST['last_name'])
    return redirect('/')