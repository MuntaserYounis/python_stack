from django.shortcuts import render,HttpResponse,redirect
from .models import User
def index(request):
    context = {
        'all_the_users': User.objects.all()
    }
    return render(request,'index.html',context)

def register(request):
    User.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],email_address=request.POST['email'],age=int(request.POST['age']))
    
    return redirect('/')
    


