from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from datetime import datetime
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        
    gold = request.session['gold']
    activities = request.session['activities']
    context= {
        'gold' : gold,
        'activites' : activities,
        
    }
    return render(request,'index.html',context)

def process(request):
    if request.POST['building'] == 'farm':
        amount = random.randint(10,20)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p") 
        text = f'You entered a farm and earned {amount} gold {timestamp}'
    elif request.POST['building'] == 'cave':
        amount = random.randint(10,20)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p") 
        text = f'You entered a cave and earned {amount} gold {timestamp}'
    elif request.POST['building'] == 'house':
        amount = random.randint(10,20)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p") 
        text = f'You entered a house and earned {amount} gold {timestamp}'
    else: 
        amount = random.randint(-50,50)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")  
        if amount > 0:
            text = f'You completed a quest and earned {amount} gold {timestamp}'
        elif amount < 0:
            text = f'You failed a quest and lost {amount} gold. Ouch {timestamp}'
        else:
            text = f'You failed a quest and lost but lost no gold. good luck next time {timestamp}'
    
    request.session['gold'] += amount
    request.session['activities'].insert(0,text)
    print(amount)
    return redirect('/')