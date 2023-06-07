from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def result(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
        'name_form' : name,
        'location_form':location,
        'language_form':language,
        'comment_form':comment
    }
    return render(request,'result.html',context)

def back(request):
    return redirect(request,'index.html')