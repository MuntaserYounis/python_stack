from django.shortcuts import render,redirect
import random
def index(request):
    if 'guess' in request.session:
        guess = request.session['guess']
    else:
        request.session['guess'] = random.randint(1,100)
        guess = request.session['guess']
    print(guess)
    context = {
        'guess' : guess
    }
    return render(request, 'index.html',context)

def process(request):
    the_guess = int(request.POST['the_guess'])
    request.session['the_guess'] = the_guess
    
    return redirect('/')

def clr(request): #not working
    request.POST['guess']
    del request.session['guess']
    return redirect('/')

