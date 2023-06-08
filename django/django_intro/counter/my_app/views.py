from django.shortcuts import render,redirect

def index(request):
    counter = request.session.get('counter',0)+1 #explain in more details 
    request.session['counter'] = counter
    
    print(counter)
    return render(request, 'index.html')

def delete(request):
    del request.session['counter']
    return redirect('/') 