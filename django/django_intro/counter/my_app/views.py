from django.shortcuts import render,redirect

def index(request):
    # counter = request.session.get('counter',0)+1 #another way of solving
    # request.session['counter'] = counter
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] = 0

    counter = request.session['counter']
    context = {
        'muntaser' : counter
    }
    print(counter)
    return render(request, 'index.html', context)

def delete(request):
    del request.session['counter']
    return redirect('/')


    