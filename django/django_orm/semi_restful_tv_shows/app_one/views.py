from django.shortcuts import render,redirect
from .models import Show
from datetime import datetime
def index(request):
    return redirect('/shows')

def all_shows(request):
    all_the_shows = Show.objects.all()
    context = {'all':all_the_shows
    }
    return render(request,'all_shows.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    date_string = request.POST['date']
    print(date_string)
    new = Show.objects.create(
        title = request.POST['title'], 
        network = request.POST['network'],
        release_date = datetime.strptime(request.POST['date'],'%Y-%m-%d'),desc = request.POST['desc'])
    new.save()
    return redirect(f'/shows/{new.id}')

def shows(request,id):
    show = Show.objects.get(id = id)
    context = {
        'show':show
    }
    return render(request,'shows.html',context)

def edit(request,id):
    this_show = Show.objects.get(id = id)
    context = {'this_show':this_show}
    return render(request,'edit.html',context)

def update(request,id):
    my_show = Show.objects.get(id=id)
    my_show.title = request.POST['title']
    my_show.network = request.POST['network']
    my_show.release_date = datetime.strptime(request.POST['date'],'%Y-%m-%d')
    my_show.desc = request.POST['desc']
    my_show.save()
    return redirect(f'/shows/{my_show.id}')

def destroy(request,id):
    to_destroy = Show.objects.get(id=id)
    to_destroy.delete()
    return redirect('/shows')