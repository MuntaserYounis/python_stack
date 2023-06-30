from django.shortcuts import render,redirect
from .models import *

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request,'index.html',context) 

def destroy(request,id):
    course = Course.objects.get(id=id)
    context = {
        'course' : course
    }
    return render(request,'destroy.html',context)

def create(request):
    the_course =Course.objects.create(name = request.POST['name'],desc = request.POST['desc'])
    the_course.save()
    return redirect('/')

def do_it(request):
    course= Course.objects.get(id = request.POST['id'])
    course.delete()
    return redirect('/')


