from django.shortcuts import render,redirect
from .models import User,Message,Comment
from django.contrib import messages
import bcrypt



def index(request):
    return render(request,'index.html')
# Create your views here.

def register(request):
    print('hi')
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
        
        
        user = User.objects.create(first_name = first_name, last_name = last_name, email= email, password = pw_hash)
        request.session['user_id'] = user.id
    return redirect('/wall')

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
            request.session['user_id'] = logged_user.id
            return redirect('/wall')
        print('Wrong Password')
    # return redirect('/wall')

# def sucess(request):
#     context = {
#         'username' : request.session['username'],
#         'status': request.session['status'],
#     }
#     return render(request,'success.html', context)

def logout(request):
    del request.session['username']
    del request.session['status']
    request.session.flush()
    return redirect('/')

def wall(request):
    context = {
        'first_name' : request.session['username'],
        'messages' : Message.objects.all(),
        'comments' : Comment.objects.all(),
    }
    return render(request, 'wall.html',context)

def add_message(request):
    message = Message.objects.create(user=User.objects.get(id =request.session['user_id']),text = request.POST['message_area'])
    message.save()
    return redirect('/wall')

def add_comment(request,id):
    new_comment = Comment.objects.create(user = User.objects.get(id = request.session['user_id']),message = Message.objects.get(id = id),content = request.POST['the_comment'])
    new_comment.save()
    return redirect('/wall')