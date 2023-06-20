from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
import bcrypt



def index(request):
    return render(request,'index.html')
# Create your views here.

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        request.session['username'] = first_name +" " + last_name
        request.session['status'] = 'registered'
        User.objects.create(first_name = first_name, last_name = last_name, email= email, password = pw_hash)
    return redirect('/success')

def login(request):
    errors2 = User.objects.login_validator(request.POST)
    if len(errors2 ) > 0:
        for key,value in errors2.items():
            messages.error(request, value)
        return redirect('/')
    
    user= User.objects.filter(email = request.POST['email2'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password2'].encode(),logged_user.password.encode()):
            request.session['username'] = logged_user.first_name
            request.session['status'] = 'logged in'
            return redirect('/success')
        print('Wrong Password')
    return redirect('/')

def sucess(request):
    context = {
        'username' : request.session['username'],
        'status': request.session['status'],
    }
    return render(request,'success.html', context)

def logout(request):
    del request.session['username']
    del request.session['status']
    request.session.flush()
    return redirect('/')
