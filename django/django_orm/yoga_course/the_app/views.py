from django.shortcuts import render,redirect
from .models import *
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
    return redirect('/classes')

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
            return redirect('/classes')
        print('Wrong Password')


def logout(request):
    del request.session['username']
    del request.session['status']
    del request.session['user_id']
    request.session.flush()
    return redirect('/')


def classes(request):
    the_courses = Course.objects.all()
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'courses' : the_courses,
        'user': user
    }
    return render(request,'classes.html',context)
def new(request):
    return render(request,'new.html')

def process(request):
    print('hi')
    errors3 = Course.objects.course_validator(request.POST)
    if len(errors3)>0:
        for key, value in errors3.items():
            messages.error(request, value)
        return redirect('/classes/new')
    else:
        title = request.POST['title']
        desc = request.POST['desc']
        day = request.POST['day']
        price = int(request.POST['price'])
        uploader = User.objects.get(id = request.session['user_id'])
        course = Course.objects.create(title = title,desc = desc, day=day , price = price,uploaded_by = uploader)
        course.save()
    return redirect('/classes')

def cancel(reuqest):
    return redirect('/classes')

def edit(request,id):
    course = Course.objects.get(id = id)
    context = {
        'course' : course
    }
    return render(request,'edit.html',context)

def process_edit(request):
    errors3 = Course.objects.course_validator(request.POST)
    if len(errors3)>0:
        for key, value in errors3.items():
            messages.error(request, value)
            course = request.POST['course_id']
            return redirect(f'/classes/{course}/edit')
    else:
        course_update = Course.objects.get(id = request.POST['course_id'])
        course_update.title = request.POST['title']
        course_update.desc = request.POST['desc']
        course_update.day = request.POST['day']
        course_update.price = int(request.POST['price'])
        course_update.save()
        return redirect('/classes')

def destroy(request):
    course_destroy = Course.objects.get(id = request.POST['course_id'])
    course_destroy.delete()
    return redirect('/classes')

def display(request,id):
    course = Course.objects.get(id = id)
    context = {
        'my_course' : course
    }
    return render(request,'display.html',context)